Title: Integrating Disqus Comment Section In Pelican Blog
Date: 2017-1-30 21:51
Modified: 2017-1-30 21:51
Category: tutorial
Tags: tutorial, pelican, disqus, commenting
Slug: integrate-disqus-in-a-post
share_post: facebook
Summary: Disqus is a worldwide blog comment hosting service for web sites and online communities that uses a networked platform.<sup>[1](https://en.wikipedia.org/wiki/Disqus)</sup> And integrating Disqus comment in pelican is straight forward and easy.

After you write a blog post, you expect people to comment in your post. Commenting is necessary because it can increase reader engagement and help build relationship among author and reader. 

Many Pelican themes support Disqus commenting natively. All you need to have is a Disqus account. Go to [disqus.com](https://disqus.com/) and quickly create an account for yourself.

Now, lets integrate Disqus to our each and every blog posts.

## Steps
 * While logged in to your Disqus account, head over to [admin create panel](https://disqus.com/admin/create/). 
 * You'll see a form. Fill up that form
 * Click **Create Site** button.
 * Now on the top left side of the page, you'll see your disqus site. Click on the link. *[refer picture below]*
 
 ![Disqus preview](images/disqus1.png)
 
 * Now headover to *setting* menu. *[refer picture below]*
 
 ![Disqus setting](images/disqus2.png)
 
 * In the setting page, you'll see the **Shortname** of youtr site as shown below.
 
 ![shortname](images/disqus3.png)
 
 * Copy that **shortname**
 
 * Now open your `pelicanconf.py` file. On that file, add the following lines:

 ```
 DISQUS_SITENAME = 'your-site-name'
 ```
 
 * Reserve your page via `$ fab reserve`
 
 * Browse the page and you'll see Disqus has been integrated to your blog post.
 
 ![disqus implemented](images/disqus4.png)
 
 ---
 
 If you're confused, see my configuration [here](https://github.com/girisagar46/girisagar46.github.io/blob/source/pelicanconf.py)
 

