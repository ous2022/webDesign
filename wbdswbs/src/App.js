import { Route, Routes } from 'react-router-dom'
import Connexion from './connexion'

const App = () => {
    return(
        <Routes>
            <Route path="/connexion" element={<Connexion />} />
        </Routes>
    )
} 

export default App