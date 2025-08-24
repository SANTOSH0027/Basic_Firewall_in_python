import random


def load_rules(filename):
    rules = {}
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                ip, action = parts
                rules[ip] = action
    return rules


def main():
    firewall_rules = load_rules("rules.txt")
    for _ in range(10):
        ip_address = getrandom_ip()
        action = check_rules(ip_address, firewall_rules)
        print(f"IP:{ip_address},Action:{action}")


def getrandom_ip():
    return f"192.168.1.{random.randint(0, 20)}"


def check_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"


if __name__ == "__main__":
    main()
