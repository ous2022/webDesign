import { Route, Routes } from 'react-router-dom'
import Connexion from './connexion'
import Inscription from './Inscription'

const App = () => {
    return(
        <Routes>
            <Route path="/connexion" element={<Connexion />} />
            <Route path="/inscription" element={<Inscription />} />
        </Routes>
    )
} 

export default App