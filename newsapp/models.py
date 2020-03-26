from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name


class PostModel(models.Model):
    title=models.CharField(max_length=255)
    posted_on=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE, related_name='posts')
    header_image=models.ImageField(upload_to='post_uploads')
    class Meta:
        verbose_name_plural='Posts'
    
    def __str__(self):
        return self.title


class CommentModel(models.Model):
    commented_on=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name_plural='Comments'

    def __str__(self):
        return self.content




