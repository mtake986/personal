import PropTypes from 'prop-types';

function Header({text, bgColor, textColor,}) {
  const headerStyles = {
    backgroundColor: bgColor,
    color: textColor 
  }
  return (
    <header style={headerStyles}>
      <div className="container">
        <h2>{text}</h2>
      </div>
    </header>
  )
}

Header.defaultProps = {
  text: 'Feedback UI', 
  bgColor: '#202142', 
  textColor: '#ff6a95'
}
Header.propTypes = {
  text: PropTypes.string,
  bgColor: PropTypes.string,
  textColor: PropTypes.string, 
}

export default Header;


// function Header({text}) {
//   return (
//     <header>
//       <div className="container">
//         <h2>{text}</h2>
//       </div>
//     </header>
//   )
// }
