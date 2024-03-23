import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home/Home';
import Account from './components/Accounts/Account';
import Bets from './components/Bets/Bets';
import Navbar from './components/Common/Navbar'; // Assuming the file is named Navbar.js

const App = () => {
  return (
    <Router>
      <div className="app">
        <header className="app-header">
          <Navbar /> {/* Replace the <nav> element with the Navbar component */}
        </header>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} exact />
            <Route path="/account" element={<Account />} />
            <Route path="/bets" element={<Bets />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
