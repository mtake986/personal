import React from 'react';
import { useHistory } from 'react-router-dom';
import { ChatEngine } from 'react-chat-engine';
import { auth } from '../firebase2';
import { useAuth } from '../contexts/AuthContext';

function Chats() {
  const history = useHistory();
  const {user } = useAuth();
  console.log(user)
  
  const handleLogout = async () => {
    await auth.signOut();
    history.push('/');
  };

  return (
    <div className='chats-page'>
      <div className='nav-bar'>
        <div className='logo-tab'>Unichat</div>
        <div onClick={handleLogout} className='logout-tab'>
          Logout
        </div>
      </div>
      <ChatEngine
        height='calc(100vh - 66px)'
        projectId='784632aa-cf90-423c-abf3-84faf8e6a692'
        userName='.'
        userSecret='.'
      />
    </div>
  );
}

export default Chats;
