import React from 'react';
import '../../styles/navbar.css';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/account">Account</Link>
        </li>
        <li>
          <Link to="/bets">Bets</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;