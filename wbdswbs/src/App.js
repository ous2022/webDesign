import { Route, Routes } from 'react-router-dom'
import Connexion from './connexion'
import Inscription from './Inscription'
import Accueil from './Components/accueil'
import ErrorPage from './Components/ErrorPage'
import ConnexionPartenaire from './ConnexionPartenaire'
import AccueilPartenaire from './Components/AccueilPartenaire'

const App = () => {
    return(
        <Routes>
            <Route path="/" element={<Accueil />} />
            <Route path="/accueil" element={<Accueil />} />
            <Route path="/connexion" element={<Connexion />} />
            <Route path='/connexionPartenaire' element={<ConnexionPartenaire />} />
            <Route path="/inscription" element={<Inscription />} />
            <Route path="/accueilPartenaire" element={<AccueilPartenaire />} />
            <Route path='/*' element={< ErrorPage />} />
        </Routes>
    )
} 

export default App