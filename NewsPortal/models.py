class Author (models.Model):
    User = models.CharField(max_length = 255)
    rating = models.FloatField(default=0.0)

class Category (models.Model):
    name_category = models.CharField(max_length = 255, unique = True)

class Post (models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # postcategory = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    article = models.CharField(max_length = 255)
    time_post = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_title = models.CharField(max_length = 255)
    article_text = models.TextField
    rating_article = models.FloatField(default=0.0)

class PostCategory (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)


