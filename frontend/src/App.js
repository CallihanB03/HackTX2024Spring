import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Home from './components/Home/Home';       // Assuming the file is named Home.js and is in the same directory
import Account from './components/Accounts/Account'; // Assuming the file is named Account.js
import Bets from './components/Bets/Bets';       // Assuming the file is named Bets.js

const App = () => {
    return (
        <Router>
            <div className="app">
                <header className="app-header">
                    <nav>
                        <Link to="/">Home</Link>
                        <Link to="/account">Account</Link>
                        <Link to="/bets">Bets</Link>
                    </nav>
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
