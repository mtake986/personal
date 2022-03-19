
import db from './firebase'
import { onSnapshot, collection, setDoc, doc, addDoc, updateDoc, deleteDoc, query, where, getDocs, serverTimestamp } from 'firebase/firestore';

// todo: add record
// Way 1: setDoc(), but overwritten and needed to specify an id
// const handleNew = async () => {
//   const docRef = doc(db, "colors", "color001");
//   const payload = {name: "Black", value: "#000"}
//   await setDoc(docRef, payload);
// }

// Way 2: addDoc(), let firestore auto-generate an id
export const handleNew = async () => {
  const name = prompt("Enter color name");
  const value = prompt("Enter color value");
  const collectionRef = collection(db, "colors");
  const payload = { name, value, timestamp: serverTimestamp() };
  const docRef = await addDoc(collectionRef, payload);
}

export const handleEdit = async (id) => {
  const name = prompt("Update a new color name");
  const value = prompt("Update a new color value");
  const docRef = doc(db, "colors", id);

  // Way 1: to add timestamp: TimeStamp()
  const payload = { name, value, timestamp: serverTimestamp() };
  setDoc(docRef, payload);

  // Way 2: use updateDoc so that a value isn't gonna be overwritten by values inside payload
  // updateDoc(docRef, payload);
  
  // I coded below before the video 3
  // const name = prompt("Update a new color name");
  // const value = prompt("Update a new color value");
  // const payload = { name, value };
  // const colorRef = doc(db, "colors", "color001");
  // await updateDoc(colorRef, payload)
}

export const handleDelete = async (id) => {
  const docRef = doc(db, "colors", id);
  await deleteDoc(docRef);
}
export const handleQueryDelete = async (id) => {
  const name = prompt("Update a new color name");
  const collectionRef = collection(db, "colors");

  const q = query(collectionRef, where("name", "==", name));
  const snapshot = await getDocs(q);
  const results = snapshot.docs.map(doc => ({ ...doc.data(), id: doc.id }))

  results.forEach(async result => {
    const docRef = doc(db, "colors", result.id);
    await deleteDoc(docRef);
  })
}


