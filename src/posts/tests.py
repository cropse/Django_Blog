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
        Checkboxtest = Entry.objects.get(title="test_checkbox")
        self.assertEqual(Checkboxtest.get_markdown(), 
"""<p>and the source code is also on <a href="www.cropse.com">Github</a>
<strong>notice: the site is on beta</strong></p>
<h3>Todo list</h3>
<hr />
<ul class="checklist">
<li><input type="checkbox" disabled> Mercury</li>
<li><input type="checkbox" disabled checked> Venus</li>
<li><input type="checkbox" disabled checked> Earth (Orbit/Moon)")</li>
</ul>""")

    def test_slug(self):
        slug_test = Entry.objects.get(title="test_p_id")
        self.assertEqual(slug_test.slug, 'test_p_id')

    def test_class(self):
        response = self.client.get('/posts/test_class/')
        self.assertContains(response, """<code class="added">testclass</code>""")
        self.assertContains(response, "<p><strong>123</strong><br />456<br /><strong>789</strong><br />012</p>")

    def test_response(self):
        response = self.client.get('/posts/test_p_id/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/base.html')
        self.assertTemplateUsed(response, 'posts/post_detail.html')
        self.assertContains(response, '<p id="title">title</p>')
        response_list = self.client.get('/posts/')
        self.assertEqual(response_list.status_code, 200)
        self.assertTemplateUsed(response_list, 'base/base.html')
        self.assertTemplateUsed(response_list, 'posts/post_list.html')
        self.assertContains(response_list, 'test')
        response_error = self.client.get('/IwantError404/')
        self.assertEqual(response_error.status_code, 404)
        self.assertTemplateUsed(response_error, 'custom404.html')
