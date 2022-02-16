// npm install packages
// import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

// import other file I have created
import Header from "./components/Header"
import FeedbackList from "./components/FeedbackList"
// import FeedbackData from './data/FeedbackData'
import FeedbackStats from './components/FeedbackStats'
import FeedbackForm from './components/FeedbackForm'
import AboutPage from './pages/AboutPage'
import AboutLinkIcon from './components/AboutLinkIcon'
import { FeedbackProvider } from './context/FeedbackContext'

function App() {
  // const [feedback, setFeedback] = useState(FeedbackData)
  // const [feedback, setFeedback] = useState(FeedbackData);

  return (
    <FeedbackProvider>
      <Router>
        <Header />
        <div className="container">
          <Routes>
            <Route
              exact
              path='/'
              element={
                <>
                  <FeedbackForm />
                  <FeedbackStats />
                  <FeedbackList />
                </>
              }>
            </Route>

            <Route path='/about' element={<AboutPage />} />

          </Routes>
          <AboutLinkIcon />
        </div>
      </Router>

    </FeedbackProvider>
  )
}
export default App;
