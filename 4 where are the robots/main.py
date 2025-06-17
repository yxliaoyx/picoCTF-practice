import requests


def main():
    base_url = "https://jupiter.challenges.picoctf.org/problem/36474/"
    robots_txt = requests.get(f"{base_url}robots.txt", timeout=30)

    for line in robots_txt.text.splitlines():
        if line.startswith("Disallow:"):
            disallowed_path = line.split(":")[1].strip()
            secret_page = requests.get(f"{base_url}{disallowed_path}", timeout=30)

            for line in secret_page.text.splitlines():
                if "picoCTF" in line:
                    print(line)


if __name__ == "__main__":
    main()
