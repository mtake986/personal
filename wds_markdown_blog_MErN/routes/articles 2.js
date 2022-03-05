const express = require('express')
const Article = require('./../models/article')
const router = express.Router()

router.get('/new', (req, res) => {
  console.log('new')
  res.render('articles/new', { article: new Article() })
  console.log('new done')
})

router.get('/edit/:id', async (req, res) => {
  const article = await Article.findById(req.params.id)
  console.log(article)
  res.render('articles/edit', { article: article })
})

router.get('/:slug', async (req, res) => {
  console.log("try")
  const article = await Article.findOne({ slug: req.params.slug })
  if (article == null) res.redirect('/')
  // console.log(article)
  res.render('articles/show', { article: article })
})

router.post('/', async (req, res, next) => {
  req.article = new Article()
  next()
}, saveArticleAndRedirect('new'))

router.put('/:id', async (req, res, next) => {
  req.article = await Article.findById(req.params.id)
  next()
}, saveArticleAndRedirect('edit'))

// method="DELETE"
router.delete('/:id', async (req, res) => {
  await Article.findByIdAndDelete(req.params.id)
  res.redirect('/')
})

function saveArticleAndRedirect(path) {
  return async (req, res) => {
    let article = req.article
    article.title = req.body.title
    article.description = req.body.description
    article.markdown = req.body.markdown
    article.sanitizedHtml = req.body.markdown
    try {
      console.log('saveArticleAndRedirect: 2')
      article = await article.save()
      console.log('saveArticleAndRedirect: 2.1')
      res.redirect(`/articles/${article.slug}`)
      console.log('saveArticleAndRedirect: 2.2')
    } catch (e) {
      console.log('saveArticleAndRedirect: 3.1')
      console.log(e) 
      res.render(`articles/${path}`, { article: article })
    }
  }
}


module.exports = router

/*
router.get('[LINK]', (req, res) => {
  res.render('[FILENAME]')
})
*/

// ? await article.save() => this is asynchronous function so we just wanna make sure we set this up inside of our own async function and we await this article that save 

// ? res.redirect(someURL) is for you want to return a 30x status code (often 302) to the browser and tell the browser to go to a new URL. This is often done on the server as part of a login process and occasionally when the user finds themselves at an old URL that has been changed to something different. res.redirect() should only be used for these types of forced navigation to a different URL and should never be part of any standard rendering process.
// ? res.render(filename, data) is how one would typically use EJS (or any other template engine plugged into Express) to fill in a template with some data and return the "rendered" HTML page back to the requesting browser so the browser can render it.