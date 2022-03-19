

import { useEffect, useState } from 'react'
import db from './firebase'
import { onSnapshot, collection, query, orderBy } from 'firebase/firestore';

import './App.css';
import Dot from './comps/Dot'
import { handleNew, handleEdit, handleDelete, handleQueryDelete } from './utils'

function App() {

  const [colors, setColors] = useState([]);

  useEffect(() => {
    const collectionRef = collection(db, "colors");
    const q = query(collectionRef, orderBy("timestamp", "desc"))
    const unsub = onSnapshot(q, (snapshot) => setColors(snapshot.docs.map((doc) => ({ ...doc.data(), id: doc.id }))))

    return unsub;
  }, [])

  // Random order
  // useEffect(
  //   () =>
  //     onSnapshot(collection(db, "colors"), (snapshot) => {
  //       setColors(snapshot.docs.map(
  //         (doc => ({
  //           ...doc.data(),
  //           id: doc.id
  //         }))
  //       ))
  //     }
  //     ), []
  // )


  return (
    <div className="App">
      <button className="create" onClick={handleNew}>
        New
      </button>
      <button className="queryDelete" onClick={handleQueryDelete}>
        Query Delete
      </button>
      <ul>
        {colors.map((color) => (
          <li key={color.id}>
            <button onClick={() => handleEdit(color.id)} >
              edit
            </button>
            <button onClick={() => handleDelete(color.id)} >
              delete
            </button>
            <Dot color={color.value} /> {color.name}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App;
