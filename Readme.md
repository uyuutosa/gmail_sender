# gmail_sender

Simple Email sender with Gmail.

## Requirements

- [emoji](https://pypi.org/project/emoji/)

## How to Use

Really simple. Just set several terms and send, thats all.

```{.python .input  n=2}
from gmail_sender import GmailSender

from_address = "sender@gmail.com" # please rewirte as you like.
password = "password"
to_address = "someone@gmail.com" # please rewrite as you like
subject = "Here is subject"
body = "Here is body"

sender = GmailSender(from_address, password)
sender.send(to_address, subject, body, attach_lst=[])
```

```{.json .output n=2}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "\u2709 Sent Email. \u2709\n"
 }
]
```

You can send Email multiple time without login.

```{.python .input  n=4}
for i in range(5):
    subject = f"No.{i} Email."
    body = ("Hello_" * i).strip("_")
    sender.send(to_address, subject, body, attach_lst=[])
```

```{.json .output n=4}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "\u2709 Sent Email. \u2709\n\u2709 Sent Email. \u2709\n\u2709 Sent Email. \u2709\n\u2709 Sent Email. \u2709\n\u2709 Sent Email. \u2709\n"
 }
]
```

If you want to attach some files, you can do by settings `attach_lst` as
follows,
(currently only supported `jpeg`, `jpg` and `png` extension)

```{.python .input  n=3}
subject = "Here is subject"
body = "Please confirm an attached file."
sender.send(to_address, subject, body, attach_lst=["path/to/image.jpg", "/path/to/image2.jpg"])
```

```{.json .output n=3}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "\u2709 Sent Email. \u2709\n"
 }
]
```

```{.python .input}

```
