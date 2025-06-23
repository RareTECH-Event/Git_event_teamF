def main():
    while True:
        print("選択してください：")
        print("1: ここなっつ")
        print("2: タイキ")
        print("3: roku")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("こんにちは")
        elif choice == "2":
            print("なにか用ですか？")
        elif choice == "3":
            print("こんばんは")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
