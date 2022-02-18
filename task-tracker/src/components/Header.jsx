// import React from 'react'
import PropTypes from 'prop-types';
import Button from './Button';
import { useLocation } from 'react-router-dom'

function Header({ title, onAdd, showAdd }) {
  const location = useLocation()

  return (
    <header className='header'>
      <h1>{title}</h1>
      {location.pathname === '/' && (
        <Button
          color={showAdd ? 'red' : 'green'}
          text={showAdd ? 'Close' : 'Add'}
          onClick={onAdd}
        />
      )}
    </header>
  );
}

Header.defaultProps = {
  title: 'React App',
};

Header.propTypes = {
  title: PropTypes.string.isRequired,
  ontoggleAddButton: PropTypes.func,
};

// CSS can be written like below and style={headingStyle}
// const headingStyle = {
//   color: 'red',
// }
export default Header;
