from playwright.sync_api import sync_playwright
import time

USERNAME = "martiii.camacho"
MAX_SCROLLS = 150

def human_scroll(page):
    page.mouse.wheel(0, 3000)
    time.sleep(2)

with sync_playwright() as p:

    browser = p.chromium.launch_persistent_context(
        user_data_dir="playwright_mobile_profile",

        executable_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",

        headless=False,

        viewport={
            "width": 390,
            "height": 844
        },

        user_agent=(
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/16.0 Mobile/15E148 Safari/604.1"
        ),

        is_mobile=True,
        has_touch=True,
        locale="es-AR"
    )

    page = browser.pages[0]

    print("Abriendo Instagram...")
    page.goto("https://www.instagram.com/", timeout=120000)

    input("\nLogeate manualmente y apretá ENTER...\n")

    print("Abriendo perfil...")
    page.goto(
        f"https://www.instagram.com/{USERNAME}/",
        wait_until="domcontentloaded",
        timeout=120000
    )

    time.sleep(5)

    print("Abriendo seguidores...")

    followers_button = page.locator("a[href$='/followers/']").first
    followers_button.click()

    time.sleep(8)

    usuarios = set()

    ultimo_total = 0
    sin_cambios = 0

    print("\nExtrayendo usuarios...\n")

    for i in range(MAX_SCROLLS):

        links = page.locator("a[href^='/']").all()

        for link in links:
            try:
                href = link.get_attribute("href")

                if (
                    href
                    and href.count("/") == 2
                    and href != "/"
                    and "explore" not in href
                    and "accounts" not in href
                    and "reel" not in href
                    and "stories" not in href
                ):
                    usuario = href.replace("/", "")
                    usuarios.add(usuario)

            except:
                pass

        print(f"Scroll {i+1} | Usuarios encontrados: {len(usuarios)}")

        if len(usuarios) == ultimo_total:
            sin_cambios += 1
        else:
            sin_cambios = 0

        ultimo_total = len(usuarios)

        if sin_cambios >= 10:
            print("\nNo aparecen más usuarios nuevos.")
            break

        try:
            human_scroll(page)

        except Exception as e:
            print("Error scroll:", e)

    archivo = f"{USERNAME}_followers_mobile.txt"

    with open(archivo, "w", encoding="utf-8") as f:
        for user in sorted(usuarios):
            f.write(user + "\n")

    print("\n==============================")
    print(f"Usuarios guardados: {len(usuarios)}")
    print(f"Archivo: {archivo}")
    print("==============================\n")

    input("ENTER para cerrar...")

    browser.close()