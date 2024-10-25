import { Link } from "react-router-dom"
import user from '../Assets/utilisateur.png'
import panier from '../Assets/panier2.png'

const Navbar = () => {
    return(
        <nav className="navbar">
            <h1>Electronik</h1>
            <div className="links">
                <Link className="navlink" to="/home">Accueil</Link>
                <Link className="navlink" to="/produit">Produit</Link>
                <Link className="navlink" to="/categorie">categorie</Link>
            </div>

            <div className="nav-right">
                <Link to="/connexion" className="nav-link"> <img src={user} alt="user" /> </Link>
                <Link to="/panier" className="nav-link">  <img src={panier} alt="panier" /> </Link>


            </div>
        </nav>
    )
}

export default Navbar