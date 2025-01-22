import React, { useEffect, useState } from 'react';
import api from './api';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        api.get('/symptoms')
            .then((response) => {
                setMessage(response.data.message);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return <h1>{message}</h1>;
}

export default App;
