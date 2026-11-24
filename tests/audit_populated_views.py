"""Browser regressions for the populated shop, learner roadmap and shared portal views."""
import os
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


def main():
    url = (Path(__file__).resolve().parents[1] / "index.html").as_uri()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel=os.getenv("ZENFORD_BROWSER", "msedge"))
        page = browser.new_page(offline=True, viewport={"width": 1280, "height": 900})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(url)
        main_view = page.locator("main")

        def visit(code):
            page.evaluate("""code => {
                if (location.hash === "#" + code) return;
                return new Promise(resolve => {
                    addEventListener("hashchange", () => resolve(true), {once: true});
                    location.hash = code;
                });
            }""", code)

        visit("SCR-M10-01")
        search = main_view.get_by_label("Tìm học liệu")
        search.fill("no match")
        expect(main_view.get_by_text("Chưa tìm thấy sản phẩm")).to_be_visible()
        main_view.get_by_role("button", name="Xóa bộ lọc").click()
        main_view.get_by_role("button", name="Trang 2").click()
        main_view.get_by_label("Ngôn ngữ", exact=True).select_option("Tiếng Anh")
        search.fill("cafe")
        expect(main_view.locator(".product-card")).to_have_count(1)
        main_view.locator("h3 a").click()
        expect(main_view.get_by_role("heading", name="Café English", exact=True)).to_be_visible()
        main_view.get_by_text("Xem trước nội dung").click()
        expect(main_view.get_by_text("Barista:", exact=False)).to_be_visible()
        main_view.get_by_role("button", name="Mua ngay").click()
        main_view.get_by_role("button", name="+", exact=True).click()
        main_view.get_by_label("Mã ưu đãi").fill("ZEN10")
        main_view.get_by_role("button", name="Áp dụng mã").click()
        expect(main_view.locator(".bill")).to_contain_text("268.200")
        main_view.get_by_role("link", name="Thanh toán", exact=True).click()
        main_view.get_by_label("Địa chỉ giao sách").fill("24 đường Hoa, TP.HCM")
        main_view.get_by_role("checkbox").check()
        expect(main_view.locator(".bill")).to_contain_text("293.200")
        main_view.get_by_role("button", name="Đặt hàng và thanh toán").click()
        main_view.get_by_role("button", name="Xác nhận thanh toán thử").click()
        expect(main_view.get_by_role("heading", name="Đã thanh toán")).to_be_visible()
        visit("SCR-M13-04")
        expect(main_view.locator("table")).to_contain_text("293.200")
        visit("SCR-M10-03")
        expect(main_view.get_by_text("Giỏ hàng đang trống")).to_be_visible()

        visit("SCR-M46-01")
        expect(main_view.locator(".road-line li")).to_have_count(4)
        main_view.get_by_role("link", name="Xem bằng chứng học tập").first.click()
        expect(main_view.get_by_text("Bài nói giới thiệu bản thân · 86/100")).to_be_visible()
        visit("SCR-M46-02")
        main_view.get_by_label("Kỳ đánh giá").select_option("Tháng 09")
        expect(main_view.get_by_text("Chưa có thay đổi trong kỳ đã chọn.")).to_be_visible()
        visit("SCR-M46-01")
        main_view.get_by_label("Lộ trình đang xem").select_option("Tiếng Nhật N5")
        expect(main_view.get_by_text("Đang bảo lưu lịch học")).to_be_visible()
        expect(main_view.locator(".road-summary")).to_have_count(0)
        visit("SCR-M46-03")
        expect(main_view.get_by_text("150 / 180")).to_be_visible()

        visit("SCR-M19-01")
        main_view.get_by_label("Tìm kiếm", exact=True).fill("Khánh An")
        main_view.get_by_role("link", name="Chi tiết", exact=True).click()
        expect(main_view.get_by_role("heading", name="Trần Khánh An")).to_be_visible()
        main_view.get_by_label("Ghi chú mới").fill("Hẹn tư vấn tối thứ Ba")
        main_view.get_by_role("button", name="Thêm ghi chú").click()
        expect(main_view.get_by_text("Hẹn tư vấn tối thứ Ba", exact=True)).to_be_visible()

        visit("SCR-M47-07")
        main_view.get_by_label("Nội dung yêu cầu").fill("Nhờ cô góp ý bài nói số ba.")
        main_view.get_by_role("button", name="Gửi", exact=True).click()
        visit("SCR-M47-08")
        expect(main_view.locator("table")).to_contain_text("Nhờ cô góp ý bài nói số ba.")
        visit("SCR-M08-05")
        main_view.get_by_label("Ngôn ngữ đánh giá").select_option("Tiếng Nhật")
        main_view.get_by_role("button", name="Bắt đầu", exact=True).click()
        main_view.get_by_label("おはようございます").check()
        main_view.get_by_role("button", name="Câu tiếp theo").click()
        main_view.get_by_label("Nhà ga ở đâu?").check()
        main_view.get_by_role("button", name="Xem kết quả").click()
        expect(main_view.get_by_text("2 / 2 câu đúng")).to_be_visible()

        visit("SCR-M13-01")
        main_view.get_by_role("button", name="Chọn gói", exact=True).last.click()
        main_view.get_by_role("button", name="Đặt mua").click()
        main_view.get_by_role("button", name="Xác nhận thanh toán thử").click()
        main_view.get_by_role("link", name="Mở gói học của tôi").click()
        expect(main_view.get_by_role("heading", name="Lớp giao tiếp")).to_be_visible()
        assert not errors, errors
        browser.close()
        print("Offline product checkout, order history, roadmap evidence, paused forecast, CRM drill-down, support request, placement and plan activation passed.")


if __name__ == "__main__":
    main()
