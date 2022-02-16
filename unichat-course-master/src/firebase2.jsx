import firebase from "firebase/app"
import "firebase/auth"

export const auth = firebase.initializeApp({
  apiKey: "AIzaSyBITtiBVZTQTI27_kiKTiHRf-IrDLBSG10",
  authDomain: "unichat-12345.firebaseapp.com",
  projectId: "unichat-12345",
  storageBucket: "unichat-12345.appspot.com",
  messagingSenderId: "304461676917",
  appId: "1:304461676917:web:1fec11160f50b95c0c533c",
  measurementId: "G-R7H384LHY6"
}).auth();
