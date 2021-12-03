from scratchclient import ScratchSession
import tkinter as tk
window = tk.Tk()

def sendComment(session, usr, comment):
    session.get_user(usr).post_comment(comment)
    return

def buttonClick():
    uName = nameEntry.get()
    password = passEntry.get()
    session = ScratchSession(uName, password)
    usr = targetEntry.get()
    comment = commentEntry.get()
    try:
        sendComment(session, usr, comment)
        button.config(text = "Success!")
    except:
        button.config(text = "An error occured!")
    
        
def main():
    nameLabel = tk.Label(window, text="Scratch Username:")
    nameEntry = tk.Entry(window)

    passLabel = tk.Label(window, text="Scratch Password:")
    passEntry = tk.Entry(window)

    targetLabel = tk.Label(window, text="Send a comment to:")
    targetEntry = tk.Entry(window)

    commentLabel = tk.Label(window, text="Comment:")
    commentEntry = tk.Entry(window)

    button = tk.Button(window, text = "Send Comment", command=buttonClick)

    nameLabel.pack()
    nameEntry.pack()
    passLabel.pack()
    passEntry.pack()
    targetLabel.pack()
    targetEntry.pack()
    commentLabel.pack()
    commentEntry.pack()
    button.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
