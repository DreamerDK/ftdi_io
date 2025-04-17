from ftio import FTIODevice
import time


def main():
    ftdio = FTIODevice("FTAO1NUQD", 0xFF)

    print(f"Initial state: 0x{ftdio.get_all():02x}")
    time.sleep(1)
    ftdio.set_all(0x00)
    print(f"All pins are set to zero: 0x{ftdio.get_all():02x}")
    time.sleep(1)

    for i in range(4, 8):
        ftdio.toggle_pin(i)
        print(f"toggle pin [{i}]: 0x{ftdio.get_all():02x}")
        time.sleep(3)
        ftdio.toggle_pin(i)
        print(f"toggle pin [{i}]: 0x{ftdio.get_all():02x}")
        time.sleep(3)


if __name__ == "__main__":
    main()
