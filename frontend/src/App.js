import React from 'react';

const App = () => {
  return (
    <div className="app">
      <header className="app-header">
        <nav>
          <button>Home</button>
          <button>Live Bets</button>
          <button>My Bets</button>
          <button>Account</button>
        </nav>
      </header>

      <div className="main-content">
        <aside className="sidebar">
          <button>Sidebar Item 1</button>
          <button>Sidebar Item 2</button>
          <button>Sidebar Item 3</button>
        </aside>
        <section className="content">
          <h1>Welcome to the Betting App</h1>
          {/* Content goes here */}
        </section>
      </div>
    </div>
  );
};

export default App;
