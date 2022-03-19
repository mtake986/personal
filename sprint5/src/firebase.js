// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getFirestore} from "firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAIF7HQR5E8QotmkXh_cO-WgqKrguz5LMY",
  authDomain: "color-palette-f2a11.firebaseapp.com",
  projectId: "color-palette-f2a11",
  storageBucket: "color-palette-f2a11.appspot.com",
  messagingSenderId: "639615800098",
  appId: "1:639615800098:web:3083b49fd1ddce94cc0b7b",
  measurementId: "G-Z12G9MW265"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export default getFirestore();