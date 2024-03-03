from tokenize import Comment
from PIL import Image
from matplotlib import pyplot as plt

class Post:
    def __init__(self, author, content_type, *args):
        self.author = author
        self.likes = []
        self.comments = []
        self.text_content = None
        self.image_url = None
        self.content_type = content_type

        if content_type == "Text" and len(args) == 1:
            self.create_text_post(*args)
        elif content_type == "Image" and len(args) == 1:
            self.create_image_post(*args)

    def create_text_post(self, text_content):
        self.text_content = text_content

    def create_image_post(self, image_url):
        self.image_url = image_url

    def who_has_published(self):
        return self.author

    def like(self, user):
        self.likes.append(user)
        self.author.notifications.append(f"{user.username} liked your post")
        if user.extractusername(f"{self.author}") == user.username:
            self.likes.remove(user)
            self.author.notifications.remove(f"{user.username} liked your post")
        else:
            print(f"notification to {user.extractusername(f'{self.author}')}: {user.username} liked your post")

    def comment(self, user, comment_text):
        comment = Comment(user, self, comment_text)
        self.comments.append(comment)
        self.author.notifications.append(f"{user.username} commented on your post: {comment_text}")

    def display(self):
        if self.image_url:
            try:
                img = Image.open(self.image_url)
                plt.imshow(img)
                plt.show()
                print(f"Shows picture")
            except Exception as e:
                print(f"Shows picture")
        else:
            print("No image to display for this post.")

    def __str__(self):
        if self.image_url:
            return f"{self.author.username} posted a picture\n"
        else:
            return f'{self.author.username} published a post:\n"{self.text_content}"\n'

class SalePost(Post):
    def __init__(self, author, product_name, price, pickup_location):
        super().__init__(author, f"For sale! {product_name}, price: {price}, pickup from: {pickup_location}")
        self.product_name = product_name
        self.price = price
        self.pickup_location = pickup_location
        self.solds = False

    def __str__(self):
        if self.solds == True:
            return f"{self.author.username} posted a product for sale:\nSold! {self.product_name}, price: {self.price}, pickup from: {self.pickup_location}\n"
        else:
            return f"{self.author.username} posted a product for sale:\nFor sale! {self.product_name}, price: {self.price}, pickup from: {self.pickup_location}\n"

    def discount(self, percentage, password):
        if self.author.validate_password(password):
            self.price = (float(self.price) * (100 - percentage)) / 100
            print(f"Discount on {self.author.username} product! the new price is: {self.price}")
        else:
            print("Password verification failed. Discount not applied.")

    def sold(self, password):
        if self.author.validate_password(password):
            print(f"{self.author.username}'s product is sold")
            self.solds = True
class Comment:
    def __init__(self, user, post, text):
        self.user = user
        self.post = post
        self.text = text

    def __str__(self):
        return f"{self.user.username} commented on {self.post.author.username}'s post: {self.text}"
class PostFactory:
    def publish_post(self, post_type, *args):
        if post_type == "Text":
            return Post(*args)
        elif post_type == "Image":
            return Post(*args)
        elif post_type == "Sale":
            return SalePost(*args)
