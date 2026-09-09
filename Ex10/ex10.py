import os
import struct

FILE_NAME = "accounts.dat"
MAX_RECORDS = 20
NAME_SIZE = 30
BANK_SIZE = 20
ADDRESS_SIZE = 100
RECORD_FORMAT = f"{BANK_SIZE}s{BANK_SIZE}s{NAME_SIZE}si{ADDRESS_SIZE}sf"
RECORD_SIZE = struct.calcsize(RECORD_FORMAT)


def pack_text(text, size):
    return text.encode("utf-8")[:size - 1].ljust(size, b"\0")


def unpack_text(data):
    return data.split(b"\0", 1)[0].decode("utf-8", errors="ignore")


def pack_account(account):
    return struct.pack(
        RECORD_FORMAT,
        pack_text(account["bank_name"], BANK_SIZE),
        pack_text(account["bank_branch"], BANK_SIZE),
        pack_text(account["name"], NAME_SIZE),
        account["number"],
        pack_text(account["address"], ADDRESS_SIZE),
        account["balance"],
    )


def unpack_account(data):
    bank, branch, name, number, address, balance = struct.unpack(RECORD_FORMAT, data)
    return {
        "bank_name": unpack_text(bank),
        "bank_branch": unpack_text(branch),
        "name": unpack_text(name),
        "number": number,
        "address": unpack_text(address),
        "balance": balance,
    }


def read_account(fp, number):
    if not 1 <= number <= MAX_RECORDS:
        return None
    fp.seek((number - 1) * RECORD_SIZE)
    data = fp.read(RECORD_SIZE)
    if len(data) != RECORD_SIZE:
        return None
    account = unpack_account(data)
    return account if account["number"] == number else None


def write_account(fp, account):
    fp.seek((account["number"] - 1) * RECORD_SIZE)
    fp.write(pack_account(account))


def display(account):
    print(f"Bank name              : {account['bank_name']}")
    print(f"Bank branch            : {account['bank_branch']}")
    print(f"Account holder name    : {account['name']}")
    print(f"Account number         : {account['number']}")
    print(f"Account holder address : {account['address']}")
    print(f"Available balance      : {account['balance']:.2f}")


def create_account(fp):
    number = int(input("Enter the account number (1 to 20): "))
    if not 1 <= number <= MAX_RECORDS:
        print("Invalid account number.")
        return
    if read_account(fp, number):
        print("Account already exists.")
        return
    account = {
        "bank_name": input("Enter the bank name              : "),
        "bank_branch": input("Enter the bank branch            : "),
        "name": input("Enter the account holder name    : "),
        "number": number,
        "address": input("Enter the account holder address : "),
        "balance": 0.0,
    }
    write_account(fp, account)
    fp.flush()
    print("\nAccount has been created successfully.\n")
    display(account)


def update_account(fp):
    number = int(input("Enter the account number to update: "))
    account = read_account(fp, number)
    if not account:
        print("Account not found.")
        return
    print("Press Enter to keep the existing value.")
    bank = input(f"Bank name [{account['bank_name']}]: ") or account["bank_name"]
    branch = input(f"Bank branch [{account['bank_branch']}]: ") or account["bank_branch"]
    name = input(f"Account holder name [{account['name']}]: ") or account["name"]
    address = input(f"Address [{account['address']}]: ") or account["address"]
    account.update(bank_name=bank, bank_branch=branch, name=name, address=address)
    write_account(fp, account)
    fp.flush()
    print("Account updated successfully.")


def delete_account(fp):
    number = int(input("Enter the account number to delete: "))
    account = read_account(fp, number)
    if not account:
        print("Account not found.")
        return
    empty = {"bank_name": "", "bank_branch": "", "name": "", "number": 0, "address": "", "balance": 0.0}
    fp.seek((number - 1) * RECORD_SIZE)
    fp.write(pack_account(empty))
    fp.flush()
    print("Account deleted successfully.")


def deposit(fp):
    number = int(input("Enter account number you want to deposit money: "))
    account = read_account(fp, number)
    if not account:
        print("Account not found.")
        return
    print(f"The current balance for account {number} is {account['balance']:.2f}")
    amount = float(input("Enter money you want to deposit: "))
    if amount < 0:
        print("Amount cannot be negative.")
        return
    account["balance"] += amount
    write_account(fp, account)
    fp.flush()
    print(f"The New balance for account {number} is {account['balance']:.2f}")


def withdraw(fp):
    number = int(input("Enter account number you want to withdraw money: "))
    account = read_account(fp, number)
    if not account:
        print("Account not found.")
        return
    print(f"The current balance for account {number} is {account['balance']:.2f}")
    amount = float(input("Enter money you want to withdraw from account: "))
    if amount < 0 or amount > account["balance"]:
        print("Invalid amount or insufficient balance.")
        return
    account["balance"] -= amount
    write_account(fp, account)
    fp.flush()
    print(f"The New balance for account {number} is {account['balance']:.2f}")


def list_accounts(fp):
    found = False
    for number in range(1, MAX_RECORDS + 1):
        account = read_account(fp, number)
        if account:
            found = True
            print("\n----------------------------")
            display(account)
    if not found:
        print("No accounts found.")


def main():
    with open(FILE_NAME, "a+b") as fp:
        while True:
            print("\n***** Welcome to Bank Application *****")
            print("1. Create new account")
            print("2. Cash Deposit")
            print("3. Cash Withdraw")
            print("4. Account Information")
            print("5. Update Account")
            print("6. Delete Account")
            print("7. Exit")
            print("8. Clear screen")
            option = input("Please enter an option: ").strip()

            if option == "1":
                create_account(fp)
            elif option == "2":
                deposit(fp)
            elif option == "3":
                withdraw(fp)
            elif option == "4":
                list_accounts(fp)
            elif option == "5":
                update_account(fp)
            elif option == "6":
                delete_account(fp)
            elif option == "7":
                break
            elif option == "8":
                os.system("cls" if os.name == "nt" else "clear")
            else:
                print("Please enter a valid option.")

if __name__ == "__main__":
    main()
