import asyncio

from playwright.async_api import async_playwright

visited_links = set()


async def traverse_links(page, url, depth, max_depth):
    if depth > max_depth or url in visited_links:
        return

    visited_links.add(url)
    await page.goto(url)
    print(f"Depth {depth}: {url}")

    # Extract all links
    links = await page.eval_on_selector_all("a", "elements => elements.map(el => el.href)")

    # Traverse each link
    for link in links:
        await traverse_links(page, link, depth + 1, max_depth)


async def main(url, max_depth):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await traverse_links(page, url, 1, max_depth)
        await browser.close()


# Example usage
url = "https://explorer.cronos.org/testnet/txs"
max_depth = 5
asyncio.run(main(url, max_depth))
