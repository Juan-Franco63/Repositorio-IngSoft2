import React, { useState } from 'react';

function Counter() {
  const [initialValue] = useState(0);
  const [count, setCount] = useState(initialValue);
  const [inputValue, setInputValue] = useState('');
  const [step, setStep] = useState(1);

  const handleIncrement = () => setCount(prev => prev + step);
  const handleDecrement = () => setCount(prev => prev - step);

  const handleInputChange = (e) => setInputValue(e.target.value);

  const handleSetValue = () => {
    const number = parseInt(inputValue, 10);
    if (!isNaN(number)) {
      setCount(number);  // Establece el contador
      setStep(number);   // Establece el paso
    }
  };

  const handleReset = () => {
    setCount(initialValue);
    setStep(1);
  };

  return (
    <div>
      <h1 data-cy="count-value">Contador: {count}</h1>
      <button onClick={handleIncrement} data-cy="btn-increment">Incrementar</button>
      <button onClick={handleDecrement} data-cy="btn-decrement">Decrementar</button>
      <br />
      <input
        type="number"
        value={inputValue}
        onChange={handleInputChange}
        data-cy="input-set"
        placeholder="Ingresa el valor"
      />
      <button onClick={handleSetValue} data-cy="btn-set">Establecer valor</button>
      <button onClick={handleReset} data-cy="btn-reset">Resetear</button>
    </div>
  );
}

export default Counter;
