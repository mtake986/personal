const express = require('express')
const mongoose = require('mongoose')
const Article = require('./models/article')
const articleRouter = require('./routes/articles')
const methodOverride = require('method-override')
const app = express()

mongoose.connect('mongodb://127.0.0.1:27017/blog', {
  useNewUrlParser: true, useUnifiedTopology: true,
})

app.set('view engine', 'ejs')

app.use(express.urlencoded({ extended: false }))
app.use(methodOverride('_method'))

app.get('/', async (req, res) => {
  const articles = await Article.find().sort({ createdAt: 'desc' })
  console.log(articles)
  res.render('articles/index', { articles: articles })
})

app.use('/articles', articleRouter)
app.listen(5000)


// ?   res.render('index', { articles: articles }) => just passing any object we want with any keys any values and this is gonna be available in our index.ejs

// ? app.use(express.urlencoded({ extended: false })) => what this is saying that we can access all of the different parameters from our artcile form inside of our article route right here (article.js in routes folder) by just accessing req.body.{whatever you call here}


// ? some ways I did to connect to MongoDB
// mongoose.connect('mongodb+srv://masa:T%40k3cl-l%215Eo@cluster0.8tjjn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', {
//   useNewUrlParser: true, useUnifiedTopology: true
// }).then(
//   () => {console.log('db connected')},
//   err => {console.log('not connected' + err)}
// )

// 2
// mongoose.connect('mongodb://localhost/blog',
//   err => {
//     if(err) throw err;
//     console.log('connected to MongoDB')
// })

// 3
// mongoose.connect('mongodb://0.0.0.0:27017/',
//   err => {
//     if(err) throw err;
//     console.log('connected to MongoDB')
// })

// 4
// var MongoClient = require('mongodb').MongoClient;
// MongoClient.connect("mongodb://localhost:27017/MyDb", function (err, db) {
//   if(err) throw err;
// });

// 5
// const mongoose = require("mongoose");
// mongoose.connect("mongodb://127.0.0.1:27017/blog")
// .then(() => {
//   console.log("Connected to Database");
// })
// .catch((err) => {
//   console.log("Not Connected to Database ERROR! ", err);
// });
