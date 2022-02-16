import { createContext, useState, useEffect } from 'react'
import { v4 as uuidv4 } from 'uuid'

const FeedbackContext = createContext()

export const FeedbackProvider = ({ children }) => {
  const [isLoading, setIsLoading ] = useState(true)
  const [feedback, setFeedback] = useState([])

  const [feedbackEdit, setFeedbackEdit] = useState({
    item: {},
    edit: false,
  })

  useEffect(() => {fetchFeedback()}, [])

  // Fetch feedback
  const fetchFeedback = async () => {
    const res = await fetch("http://localhost:3000/feedback?_sort=id&_order=desc")
    const data = await res.json()

    setFeedback(data);
    setIsLoading(false)
  }
  // Function: addFeedback
  const addFeedback = (newFeedback) => {
    newFeedback.id = uuidv4()
    setFeedback([newFeedback, ...feedback])
  }

  // Function: deleteFeedback
  const deleteFeedback = (id) => {
    if (window.confirm('Are you sure you want to delete?')) {
      setFeedback(feedback.filter((item) => item.id !== id))
    }
  }

  // Update feedback items
  const updateFeedback = (id, updItem) => {
    // console.log(id, updItem)
    setFeedback(feedback.map((item) => item.id === id ? { ...item, ...updItem} : item))
  }

  // Set item edited
  const editFeedback = (item) => {
    setFeedbackEdit({ item, edit: true })
  }
  return <FeedbackContext.Provider
    value={{
      feedback,
      feedbackEdit,
      isLoading,    
      addFeedback,
      deleteFeedback,
      editFeedback,
      updateFeedback, 
    }}>
    {children}
  </FeedbackContext.Provider>
}

export default FeedbackContext