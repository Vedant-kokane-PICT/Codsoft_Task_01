from nltk.chat.util import Chat, reflections
import tkinter as tk
from nltk.chat.util import Chat, reflections
name = ""
chatPairs = [
    [
        r"hello|hi|hey|Hi|Hello|hey",
        ["Hello  how can, I help you"]
    ],
    [
        r"whats your name|your name|what is your name|tell me your name|what is ur name",
        ["My name is jojo"]
    ],
    [
        r"my name is (.*)|hi i am (.*)",
        ['hello %1. , how may I help you - ']
    ],
    [
        r"i am (.*)",
        ['hello %1. , how may I help you - ']
    ],
    [
        r"problem with orders|problem order|order did not recived|complaint order|problem with order|order complaint|order|i have problems with order|I have problems with my order",
        ['So you have problems with the orders, I will  help you just tell me the order id ']
    ],
    [
        r"id (.*)",
        ['I got your order id %1. I am sending a request to the customer care department']
    ],
    [
        r"thank you|tnx|TNX|thanks|Thanks",
        ['I am happy to help you']
    ],
    [
        r'exit|bye|end|end chat',
        ['Bye hope you reviced help']
    ],
    [
        r'i have problems|i have problem|i have problems|problems|problem',
        ['Please specify the problem']
    ],
    [
        r'i need help|i need some help|help|some help',
        ['Please specify the problem for which you need help']
    ],
    [
        r'i need help|i need some help|help|some help',
        ['Please specify the problem for which you need help']
    ],
    [
        r'i need a laptop|i need a new phone|i need a phone|i want to buy something|i need laptop|phone|laptop',
        ['Sure, you will be navigated to the shop section']
    ],
    [
        r"problem with cart|problem cart|complaint cart|problem with cart|cart complaint|order|i have problems with cart|I have problems with my cart|cart",
        ['So you have problems with the orders, I will  help you just tell me the order id ']
    ],
    [
        r'',
        ['I do not have any idea regarding your question Please contact customer@Ecom.com']
    ]
]

# def chat():
#     print("Hello , I am jojo how may I help you")
#     object = Chat(chatPairs,reflections)
#     object.converse()

# chat()


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ecomm Website Chat bot")
        self.chat_window = tk.Text(self.master, height=20, width=130)
        self.scrollbar = tk.Scrollbar(
            self.master, command=self.chat_window.yview)
        self.chat_window.configure(yscrollcommand=self.scrollbar.set)
        self.user_input = tk.Entry(self.master, width=90)
        self.send_button = tk.Button(
            self.master, text="Send", command=self.send_message)

        self.chat_window.pack()
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.user_input.pack()
        self.send_button.pack()

        self.conversation = Chat(chatPairs, reflections)
        self.chat_window.insert(
            tk.END, "Hello, I am jojo from Ecomm How can I help you?\n")
        self.chat_window.insert(
            tk.END, "If you have problems with order or wanna know any information about the product then please ask for it.\n")
        self.user_input.bind('<Return>', self.send_message)

    def send_message(self, event=None):
        user_query = self.user_input.get()
        user_query = user_query.lower()
        self.user_input.delete(0, tk.END)
        self.chat_window.insert(tk.END, "You: " + user_query + "\n")
        response = self.conversation.respond(user_query)
        self.chat_window.insert(tk.END, "jojo: " + response + "\n")

        if user_query.lower() == 'exit' or user_query.lower() == 'end' or user_query.lower() == 'stop' or user_query.lower() == 'bye':
            self.master.quit()

        self.chat_window.yview(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    chatbot_gui = ChatbotGUI(root)
    root.mainloop()
