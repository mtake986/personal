import React from 'react';
import Card from '../components/shared/Card';
import { Link } from 'react-router-dom';

function AboutPage() {
  return (
    <Card>
      <div className='about'>
        <h1>About this project</h1>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ad expedita
          reiciendis natus veritatis fuga consequuntur? Eius, quasi dolore? Id
          atque repellendus corporis illum consequatur quaerat sapiente
          reiciendis natus itaque odit.
        </p>
      </div>
      <h1>Masahiro Takechi</h1>
      <h2>Born and raised in Kochi</h2>
      <p>
        <Link to='/'>Back to home</Link>
      </p>
    </Card>
  );
}

export default AboutPage;
