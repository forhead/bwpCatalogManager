import tkinter as tk
import json
import os
import subprocess

def save_config(clientid, clientsecret, targetid):
    config = {
        "clientid": clientid,
        "clientsecret": clientsecret,
        "targetid": targetid
    }
    try:
        with open("config.json", "w") as f:
            json.dump(config, f)
        print("配置信息已成功保存到 config.json")
    except Exception as e:
        print(f"保存配置信息时出错: {e}")

def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return None

def show_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("设置")
    settings_window.geometry("300x300")

    tk.Label(settings_window, text="Client ID:").pack(pady=5)
    clientid_entry = tk.Entry(settings_window)
    clientid_entry.pack(pady=5)

    tk.Label(settings_window, text="Client Secret:").pack(pady=5)
    clientsecret_entry = tk.Entry(settings_window, show="*")
    clientsecret_entry.pack(pady=5)

    tk.Label(settings_window, text="Target ID:").pack(pady=5)
    targetid_entry = tk.Entry(settings_window)
    targetid_entry.pack(pady=5)

    def save():
        clientid = clientid_entry.get()
        clientsecret = clientsecret_entry.get()
        targetid = targetid_entry.get()
        save_config(clientid, clientsecret, targetid)
        settings_window.destroy()

    save_button = tk.Button(settings_window, text="保存", command=save)
    save_button.pack(pady=10)

    # 加载配置信息
    config = load_config()
    if config:
        clientid_entry.insert(0, config.get("clientid", ""))
        clientsecret_entry.insert(0, config.get("clientsecret", ""))
        targetid_entry.insert(0, config.get("targetid", ""))

def show_home():
    # 清除当前页面内容，但保留按钮框架
    for widget in main_frame.winfo_children():
        if widget!= button_frame:
            widget.destroy()
    # 这里可以添加主页的其他内容，目前保持空白
    pass

def show_search():
    def perform_search():
        # 暂时放空搜索逻辑
        print("执行搜索，使用以下条件：")
        print(f"AmazonSkuProductIdentifierInput: {amazon_sku_entry.get()}")
        print(f"externalId: {external_id_entry.get()}")
        print(f"productId: {productId_entry.get()}")
        print(f"sku: {sku_entry.get()}")

    def show_product_details():
        product_details_window = tk.Toplevel(root)
        product_details_window.title("产品详情")
        tk.Label(product_details_window, text="产品详情页面").pack(pady=10)
        # 这里可以添加产品的具体信息
        update_button = tk.Button(product_details_window, text="更新", command=update_product)
        update_button.pack(pady=10)
        delete_button = tk.Button(product_details_window, text="删除", command=delete_product)
        delete_button.pack(pady=10)

    def update_product():
        print("更新产品逻辑")

    def delete_product():
        print("删除产品逻辑")

    # 清除当前页面内容，但保留按钮框架
    for widget in main_frame.winfo_children():
        if widget!= button_frame:
            widget.destroy()

    tk.Label(main_frame, text="搜索页面").pack(pady=10)
    amazon_sku_entry = tk.Entry(main_frame)
    amazon_sku_entry.pack(pady=5)
    external_id_entry = tk.Entry(main_frame)
    external_id_entry.pack(pady=5)
    productId_entry = tk.Entry(main_frame)
    productId_entry.pack(pady=5)
    sku_entry = tk.Entry(main_frame)
    sku_entry.pack(pady=5)
    search_button = tk.Button(main_frame, text="搜索", command=perform_search)
    search_button.pack(pady=10)

    # 假设搜索结果显示在一个列表中
    result_listbox = tk.Listbox(main_frame)
    result_listbox.pack(pady=10)
    # 假设这里有一些搜索结果
    result_listbox.insert(tk.END, "产品 1")
    result_listbox.insert(tk.END, "产品 2")
    result_listbox.bind('<<ListboxSelect>>', lambda event: show_product_details())

def show_new():
    def save_new():
        print("保存新建的内容")
        # 这里可以添加保存逻辑，根据输入更新 GraphQL 变量
        print(f"externalId: {external_id_new_entry.get()}")
        print(f"sku: {sku_new_entry.get()}")
        print(f"amazonSku: {amazon_sku_new_entry.get()}")
        print(f"detailPageUrl: {detail_page_url_entry.get()}")
        print(f"imageUrl: {image_url_entry.get()}")
        print(f"imageAltText: {image_alt_text_entry.get()}")

    # 清除当前页面内容，但保留按钮框架
    for widget in main_frame.winfo_children():
        if widget!= button_frame:
            widget.destroy()

    tk.Label(main_frame, text="新建页面").pack(pady=10)
    external_id_new_entry = tk.Entry(main_frame)
    external_id_new_entry.pack(pady=5)
    sku_new_entry = tk.Entry(main_frame)
    sku_new_entry.pack(pady=5)
    amazon_sku_new_entry = tk.Entry(main_frame)
    amazon_sku_new_entry.pack(pady=5)
    detail_page_url_entry = tk.Entry(main_frame)
    detail_page_url_entry.pack(pady=5)
    image_url_entry = tk.Entry(main_frame)
    image_url_entry.pack(pady=5)
    image_alt_text_entry = tk.Entry(main_frame)
    image_alt_text_entry.pack(pady=5)
    offer_prime_checkbox = tk.Checkbutton(main_frame, text="Offer Prime", onvalue=True, offvalue=False)
    offer_prime_checkbox.pack(pady=5)
    save_button = tk.Button(main_frame, text="保存", command=save_new)
    save_button.pack(pady=10)

def create_buttons():
    global button_frame
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.X)

    # 加载图标文件，需要准备相应的图标文件
    home_icon = tk.PhotoImage(file="home_icon.png")
    search_icon = tk.PhotoImage(file="search_icon.png")
    new_icon = tk.PhotoImage(file="new_icon.png")
    settings_icon = tk.PhotoImage(file="settings_icon.png")

    home_button = tk.Button(button_frame, text="主页", image=home_icon, compound=tk.TOP, command=show_home, height=30, width=60)
    home_button.image = home_icon
    home_button.pack(side=tk.LEFT)
    search_button = tk.Button(button_frame, text="搜索", image=search_icon, compound=tk.TOP, command=show_search, height=30, width=60)
    search_button.image = search_icon
    search_button.pack(side=tk.LEFT)
    new_button = tk.Button(button_frame, text="新建", image=new_icon, compound=tk.TOP, command=show_new, height=30, width=60)
    new_button.image = new_icon
    new_button.pack(side=tk.LEFT)
    settings_button = tk.Button(button_frame, text="设置", image=settings_icon, compound=tk.TOP, command=show_settings, height=30, width=60)
    settings_button.image = settings_icon
    settings_button.pack(side=tk.LEFT)

    # 添加批量上传按钮
    upload_icon = tk.PhotoImage(file="upload_icon.png")
    upload_button = tk.Button(button_frame, text="批量上传", image=upload_icon, compound=tk.TOP, command=batch_upload, height=30, width=80)
    upload_button.image = upload_icon
    upload_button.pack(side=tk.LEFT)

def main():
    global root, main_frame
    root = tk.Tk()
    root.title("主界面")
    root.geometry("500x500")

    # 尝试加载配置
    config = load_config()
    if config:
        print("已加载配置:", config)

    # 创建按钮
    create_buttons()

    # 创建主框架，用于切换页面
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # 显示主页
    show_home()

    root.mainloop()

def batch_upload():
    # 调用 catalog_upload.sh 脚本进行批量上传
    subprocess.call(["sh", "catalog_upload.sh"])

if __name__ == "__main__":
    main()