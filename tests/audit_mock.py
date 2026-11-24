"""Offline browser checks. Requires Playwright and a local Chromium browser."""

import os
from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    url = (Path(__file__).resolve().parents[1] / "index.html").as_uri()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel=os.getenv("ZENFORD_BROWSER", "msedge"))
        context = browser.new_context(offline=True)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(url)

        for width in (390, 1440):
            page.set_viewport_size({"width": width, "height": 900})
            issues = page.evaluate("""() => {
              const issues = [];
              for (const screen of data.screens) {
                history.replaceState(null, "", "#" + screen.id);
                render();
                if (innerWidth === 1440) {
                  const instructions = new Set(screen.el.filter(text => text.length >= 38));
                  for (const node of main.querySelectorAll("h2,h3,p,button,summary,legend")) {
                    if (instructions.has(node.textContent.trim()))
                      issues.push([screen.id, "wireframe instruction displayed as content"]);
                  }
                }
                if (!main.querySelector("h1")) issues.push([screen.id, "missing heading"]);
                if (document.documentElement.scrollWidth > innerWidth + 1)
                  issues.push([screen.id, "horizontal overflow"]);
                for (const a of main.querySelectorAll('a[href^="#"]')) {
                  const destination = a.hash.slice(1);
                  if (!screens.has(destination) && !["danh-muc","pre-done","main"].includes(destination))
                    issues.push([screen.id, destination]);
                }
              }
              return issues;
            }""")
            assert not issues, issues
            print(f"All screen routes, internal links and page widths passed at {width}px.")

        page.goto(url)
        def visit(code):
            page.evaluate("""code => {
              if (location.hash === "#" + code) return;
              return new Promise(resolve => {
                addEventListener("hashchange", () => resolve(true), {once:true});
                location.hash = code;
              });
            }""", code)

        def minh_report():
            visit("SCR-M42-07")
            return page.locator("tr").filter(has_text="Minh Anh").inner_text()

        assert "Chưa đủ dữ liệu" in minh_report()
        visit("SCR-M42-02")
        page.get_by_role("radio").first.check()
        page.get_by_role("button", name="Kiểm tra câu trả lời").click()
        assert "Cần luyện thêm" in page.locator("main .note").inner_text()
        assert "Chưa đủ dữ liệu" in minh_report()
        visit("SCR-M42-02")
        page.get_by_role("button", name="Câu tiếp theo").click()
        page.get_by_label("Câu trả lời").fill("incorrect")
        page.get_by_role("button", name="Kiểm tra câu trả lời").click()
        page.get_by_role("button", name="Câu tiếp theo").click()
        page.get_by_role("button", name="Dùng bản ghi mẫu").click()
        page.get_by_role("button", name="Kiểm tra câu trả lời").click()
        page.get_by_role("button", name="Xem kết quả").click()
        assert "Chưa ghi nhận" in page.locator(".note.mint").inner_text()
        page.get_by_role("button", name="Làm lại chẩn đoán").click()
        page.get_by_role("radio").nth(1).check()
        page.get_by_role("button", name="Kiểm tra câu trả lời").click()
        page.get_by_role("button", name="Câu tiếp theo").click()
        page.get_by_label("Câu trả lời").fill("Could")
        page.get_by_role("button", name="Kiểm tra câu trả lời").click()
        page.get_by_role("button", name="Câu tiếp theo").click()
        page.get_by_role("button", name="Dùng bản đọc đúng trọng âm").click()
        page.get_by_role("button", name="Kiểm tra câu trả lời").click()
        page.get_by_role("button", name="Xem kết quả").click()
        page.get_by_role("link", name="Vào luyện tập").click()
        page.get_by_role("button", name="Dùng bản ghi mẫu").click()
        page.get_by_role("button", name="Hoàn thành Pre-class").click()
        assert "Chưa đủ dữ liệu" not in minh_report()

        visit("SCR-M17-04")
        def click(label):
            page.get_by_role("button", name=label, exact=True).click()

        click("Chạy bước")
        click("Hoàn thành bước")
        click("Chuyên gia duyệt")
        click("Chạy bước")
        click("Mô phỏng kiểm định trả về")
        click("Chạy lại bước")
        visit("SCR-M17-06")
        comparison = page.locator("main table").inner_text()
        assert "Thiết kế khung" in comparison and "Audio" not in comparison
        assert "v1 → v2" in comparison
        visit("SCR-M16-12")
        assert page.locator('[data-action="academic-final"]').count() == 0

        visit("SCR-M29-04")
        assert page.evaluate("""() => criteria.reduce((sum,c)=>sum+c[1],0)===100
          && candidates.every(c=> c.score===null ? c.scores.every(v=>v===null)
             : c.score===c.scores.reduce((sum,v)=>sum+v,0))""")
        page.locator("#cv-filter").select_option("Cần xem lại")
        page.locator("#cv-band").select_option("Dưới 75 điểm")
        assert page.locator("#cv-table tbody tr").count() == 1
        assert "Trần Bình" in page.locator("#cv-table").inner_text()
        for excerpt in page.locator("main blockquote").all_text_contents():
            assert excerpt.strip("“”") in page.locator(".sheet").inner_text()
        page.locator("#cv-band").select_option("Từ 75 điểm")
        assert "Không có hồ sơ phù hợp" in page.locator("main").inner_text()
        assert not errors, errors
        print("Learning evidence, curriculum revision, approval gate and CV data checks passed.")
        browser.close()


if __name__ == "__main__":
    main()
