#图书管理系统 控制台版
import os
#全局变量：存放图书室信息[书名，作者，库存]
book_list = []
#数据保存文件
FILE_PATH = "book_data.txt"
#加载文件数据
def load_data() :
    if os.path.exists(FILE_PATH) :
        with open(FILE_PATH, "r", encoding="utf-8") as f :
            for line in f :
                line = line.strip()
                if line :
                    name, author, count = line.split(",")
                    book_list.append([name, author, count])
#保存数据文件
def save_data() :
    with open(FILE_PATH, "w", encoding="utf-8") as f :
        for book in book_list :
            f.write(f"{book[0]},{book[1]},{book[2]}\n")
#添加图书
def add_book() :
    name = input("请添加图书名")
    author = input("请输入图书作者")
    count = input("请输入图书库存")
    book_list.append([name, author, count])
    save_data()
    print("图书添加成功")
#查询所有图书
def show_book() :
    if not book_list :
        print("暂无图书数据")
        return
    print("\n=====图书列表=====")
    for idx, book in enumerate(book_list) :
        print(f"编号：{idx + 1}| 书名：{book[0]}| 作者：{book[1]}| 库存： {book[2]}")
    print("================\n")
#借书
def borrow_book() :
    show_book()
    idx = int(input("请输入你要查询的图书编号")) - 1
    if 0 <= idx < len(book_list) :
        book = book_list[idx]
        if book == book_list[2] > 0:
              book_list[idx][2] = str(int(book_list[2] - 1))
              save_data()
              print("借书成功")
        else :
               print("库存不足，无法借阅")
    else :
      print("编号不存在")
#还书
def return_book() :
    show_book()
    idx = int(input("请输入你要还的")) - 1
    if 0 <= idx < len(book_list) :
        book_list[idx][2] = str(int(book_list[idx][2] + 1))
        save_data()
        print("还书成功")
    else :
        print("编号不存在")
#主菜单
def main_menu() :
    load_data()
    while True :
        print("\n=====图书管理系统=====")
        print("1. 添加图书")
        print("2. 查询图书")
        print("3. 借阅图书")
        print("4. 归还图书")
        print("5. 退出图书系统")
        print("====================")
        choice = input("请输入功能编号")
        if choice == "1" :
            add_book()
        elif choice == "2" :
            show_book()
        elif choice == "3" :
            borrow_book()
        elif choice == "4" :
            return_book()
        elif choice == "5" :
            print("退出系统")
            break
        else :
            print("输入有误，请重新输入")
if __name__ == "__main__":
    main_menu()