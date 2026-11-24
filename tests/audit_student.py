"""Offline regression checks for the customer's HV-01–23 learner portal."""

import os
import re
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
URL = (ROOT / "index.html").as_uri()
REFERENCE = ROOT / "Cổng học viên Zenford - nháp1.html"


def main():
    inventory = re.findall(r"\['([\w-]+)','(HV-\d+)','([^']+)'", REFERENCE.read_text(encoding="utf-8"))
    assert len(inventory) == 23
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel=os.getenv("ZENFORD_BROWSER", "msedge"))
        page = browser.new_page(offline=True, reduced_motion="reduce")
        page.set_default_timeout(5000)
        errors, requests = [], []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: requests.append(request.url) if request.url.startswith(("http:", "https:")) else None)
        page.goto(URL + "#HV-01")
        portal = page.frame_locator("#student-host iframe")
        body = portal.locator("#page")

        def visit(fragment):
            page.evaluate("id => location.hash = id", fragment)

        for width in (390, 1440):
            page.set_viewport_size({"width": width, "height": 850})
            for slug, hv, title in inventory:
                visit(hv)
                expect(portal.locator("#crumb")).to_have_text(title)
                expect(body.locator("h1")).to_have_count(1)
                assert body.evaluate("e => e.ownerDocument.documentElement.scrollWidth <= innerWidth + 1"), (width, slug)
                if slug == "lich" and width == 390:
                    assert portal.locator(".week").bounding_box()["width"] > 300

        # The host owns browser history even when a link is followed inside the portal.
        visit("HV-01")
        body.locator('a[href="#check-in"]').first.click()
        page.wait_for_url(URL + "#SCR-M42-01")
        page.go_back()
        expect(portal.locator("#crumb")).to_have_text("Hôm nay")
        page.go_forward()
        portal.locator('[data-emo="happy"]').click()
        for _ in range(3):
            portal.locator("[data-next]").click()
        for question, answer in enumerate([1, 0, 1, 0]):
            portal.locator(f'[data-q="{question}"][data-o="{answer}"]').click()
        portal.locator("[data-finish]").click()
        expect(body).to_contain_text("Sẵn sàng 100%")
        body.get_by_role("link", name="Xem buổi học").click()
        expect(body).to_contain_text("sẵn sàng 100%")
        visit("HV-04")
        expect(body).to_contain_text("+0 câu")

        visit("SCR-M39-04")
        portal.locator('[data-slot="0"]').click()
        portal.locator("#confirm-slot").click()
        expect(body).to_contain_text("Ca bạn vừa đăng ký")
        visit("HV-01")
        visit("HV-05")
        expect(body.locator(".held-slot")).to_contain_text("30/11")
        body.get_by_role("button", name="Hủy đăng ký").click()
        expect(body.locator(".held-slot")).to_have_count(0)

        visit("HV-11")
        expect(body.locator("[data-ans]")).to_have_count(0)
        body.locator('[data-ev="2"]').click()
        body.locator('[data-ans="1"]').click()
        expect(body).to_contain_text("bằng chứng cũng đúng")
        visit("HV-14")
        body.locator("#vq").fill("because")
        expect(body.locator("article")).to_have_count(1)
        body.get_by_role("button", name="Thêm ghi chú").click()
        portal.locator("#personal-note").fill("<b>ghi chú riêng</b>")
        portal.locator("#save-note").click()
        expect(body).to_contain_text("<b>ghi chú riêng</b>")

        body.locator("#flash").click()
        for _ in range(12):
            portal.locator("#card").click()
            portal.locator('[data-delay="4320"]').click()
        expect(portal.locator("#fc")).to_contain_text("đã ôn xong 12 thẻ")
        portal.get_by_role("button", name="Về Vở AI").click()
        expect(body.locator("#flash")).to_be_disabled()

        visit("HV-13")
        body.locator("#hzi").fill("<b>Câu hỏi</b>")
        body.get_by_role("button", name="Gửi", exact=True).click()
        expect(body.locator(".msg.me").last).to_have_text("<b>Câu hỏi</b>")
        expect(body.locator(".msg.me b")).to_have_count(0)

        visit("HV-15")
        body.get_by_role("link", name=re.compile("Café English")).click()
        expect(page.locator("main")).to_contain_text("A seat by the window")
        page.get_by_role("button", name="Chương tiếp").click()
        expect(page.locator("main")).to_contain_text("Ordering at a café")
        page.go_back()
        expect(portal.locator("#crumb")).to_have_text("Thư viện của bạn")

        visit("HV-19")
        expect(body.locator("#auto")).to_have_attribute("aria-checked", "false")
        body.locator('[data-per="3"]').click()
        expect(body.locator(".sumrow.t")).to_contain_text("1.111.500")
        body.locator("#paynow").click()
        portal.get_by_role("button", name="Xác nhận thanh toán mẫu").click()
        expect(body.locator(".tbl tbody tr").first).to_contain_text("1.111.500")
        body.locator('[data-renew="ja"][data-chg]').click()
        body.locator('[data-mode="hyb"]').click()
        expect(body.locator(".sumrow.t")).to_contain_text("380.000")
        body.locator("#payer-learner").select_option("Gia Hân")
        expect(body).to_contain_text("Đang bảo lưu")

        visit("HV-21")
        body.locator("#nightsw").click()
        expect(portal.locator("html")).to_have_attribute("data-theme", "dark")
        portal.locator("#langchip").click()
        portal.locator('[data-lang="ja"]').click()
        visit("HV-06")
        expect(body).to_contain_text("Chưa có bài học mẫu cho tiếng Nhật")
        body.locator("#use-en").click()
        expect(body.locator(".kgrid button")).to_have_count(12)

        page.set_viewport_size({"width": 390, "height": 850})
        portal.locator('.tabbar [data-r="more"]').click()
        expect(portal.locator("#modal nav").first.locator("a")).to_have_count(23)
        portal.locator('#modal a[href="#website"]').click()
        page.wait_for_url(URL + "#SCR-M08-01")
        expect(page.locator("header.top")).to_be_visible()
        expect(page.locator("#student-host")).to_be_hidden()
        assert not errors and not requests, (errors, requests)
        browser.close()
        print("23 customer screens passed at 390px and 1440px, with offline navigation, learner state, billing and library checks.")


if __name__ == "__main__":
    main()
