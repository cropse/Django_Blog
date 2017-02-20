from django.test import TestCase
from zinnia.models import Entry


class EntryTestCase(TestCase):
    def setUp(self):
        Entry.objects.create(title="test_p_id", content="""
title\n{: #title}""")
        Entry.objects.create(title="test_checkbox", content="""
and the source code is also on [Github][BlogGithub]
**notice: the site is on beta**
### Todo list
---
- [ ] Mercury
- [x] Venus
- [x] Earth (Orbit/Moon)")
[BlogGithub]: www.cropse.com
""")
        Entry.objects.create(title="test_class", content="""**123**\n456\n**789**\n012\n
`testclass`{: .added}""")

    def test_entry_checkbox(self):
        response = self.client.get('/posts/test_checkbox/')
        # print(response.content)
        self.assertContains(response, """<li><input type="checkbox" disabled> Mercury</li>\n<li><input type="checkbox" disabled checked> Venus</li>\n<li><input type="checkbox" disabled checked> Earth (Orbit/Moon)")</li>""")

    def test_slug(self):
        slug_test = Entry.objects.get(title="test_p_id")
        self.assertEqual(slug_test.slug, 'test_p_id')

    def test_class(self):
        response = self.client.get('/posts/test_class/')
        self.assertContains(response, """<code class="added">testclass</code>""")
        # print(response.content)
        self.assertContains(response, "<p><strong>123</strong><br />\n456<br />\n<strong>789</strong><br />\n012</p>")

    def test_response(self):
        response = self.client.get('/posts/test_p_id/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/base.html')
        self.assertTemplateUsed(response, 'posts/post_detail.html')
        self.assertContains(response, '<p id="title">title<br /></p>')
        response_list = self.client.get('/posts/')
        self.assertEqual(response_list.status_code, 200)
        self.assertTemplateUsed(response_list, 'base/base.html')
        self.assertTemplateUsed(response_list, 'posts/post_list.html')
        self.assertContains(response_list, 'test')
        response_error = self.client.get('/IwantError404/')
        self.assertEqual(response_error.status_code, 404)
        self.assertTemplateUsed(response_error, 'custom404.html')
