import React from 'react';

const Home = () => {
    return <div>
        <h1>Home Page Content</h1>
        <p>Welcome to the home page of our app!</p>

        <div>
            <div>
                <h2>Current Account Balance: </h2>
                <div>
                    <h3>Total Balance: $PLACEHOLDER$</h3>
                    <h3>Sports Betting Balance: $PLACEHOLDER$</h3>
                </div>
            </div>
            <div>
                <h2>Ratio of Total Balance and Sports Betting Balance</h2>
                <div>
                    $PLACEHOLDER$ {/* Pie chart component */}
                </div>
            </div>
            <div>
                <h2>Performance of Bets Over Time</h2>
                <div>
                    $PLACEHOLDER$ {/* Graph component */}
                </div>
            </div>
        </div>
    </div>;
};

export default Home;
