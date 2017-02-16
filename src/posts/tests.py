from django.test import TestCase
from zinnia.models import Entry


class EntryTestCase(TestCase):
    def setUp(self):
        Entry.objects.create(title="test", content="#Title Test \n 123")
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
        # print(Entry.objects.get(title="test_checkbox").get_markdown())

    def test_entry_markdown(self):
        Entrytest = Entry.objects.get(title="test")
        Checkboxtest = Entry.objects.get(title="test_checkbox")
        self.assertEqual(Entrytest.get_markdown(), '<h1>Title Test</h1>\n<p>123</p>')
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
        slug_test = Entry.objects.get(title="test")
        self.assertEqual(slug_test.slug, 'test')

    def test_response(self):
        response = self.client.get('/posts/test/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/base.html')
        self.assertTemplateUsed(response, 'posts/post_detail.html')
        self.assertContains(response, '<h1>Title Test</h1>\n<p>123</p>')
        response_list = self.client.get('/posts/')
        self.assertEqual(response_list.status_code, 200)
        self.assertTemplateUsed(response_list, 'base/base.html')
        self.assertTemplateUsed(response_list, 'posts/post_list.html')
        self.assertContains(response_list, 'test')
        response_error = self.client.get('/IwantError404/')
        self.assertEqual(response_error.status_code, 404)
        self.assertTemplateUsed(response_error, 'custom404.html')
