import React, { useState } from 'react';

const Account = () => {
  const [balance, setBalance] = useState(100.00);
  const [amount, setAmount] = useState('');
  const [error, setError] = useState('');
  const [sliderValue, setSliderValue] = useState(50);

  const handleDeposit = () => {
    const depositAmount = parseFloat(amount);
    if (!isNaN(depositAmount)) {
      setBalance(balance + depositAmount);
      setAmount('');
    }
  };

  const handleWithdraw = () => {
    const withdrawAmount = parseFloat(amount || sliderValue); // Use amount input if not empty, otherwise use slider value
    if (!isNaN(withdrawAmount) && withdrawAmount <= balance) {
      setBalance(balance - withdrawAmount);
      setAmount('');
    } else {
      setError('Withdraw amount exceeds the current balance.');
      setTimeout(() => {
        setError('');
      }, 5000); // Hide error message after 5 seconds
    }
  };

  const handleSliderChange = (event) => {
    setSliderValue(parseInt(event.target.value));
  };

  return (
    <div className="account-container">
      <h2>Welcome to Your Account</h2>
      <p>Your current balance: ${balance.toFixed(2)}</p>
      <p>Slider value: {sliderValue}%</p>
      <input
        type="range"
        min="0"
        max="100"
        value={sliderValue}
        onChange={handleSliderChange}
      />
      <br />
      <input
        type="number"
        placeholder="Enter amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button onClick={handleDeposit}>Deposit</button>
      <button onClick={handleWithdraw}>Withdraw</button>
      {error && <p className="error">{error}</p>}
    </div>
  );
};

export default Account;
