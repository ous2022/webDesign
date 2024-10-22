import { Link } from "react-router-dom"
import Navbar from "../utils/navBarre"
import loupe from "../Assets/chercher.png"

const Accueil = () => {
    return(
        <>
            <Navbar />
            <main>
                <div className="firstmain">
                    <div className="searchBar">
                        <input type="search" placeholder="Recherchez un produit" />
                        <button><img src={loupe}  alt="recherche" /></button>

                    </div>
                    <div className="logo">
                        <h1>Electronic</h1>
                    </div>

                    <Link className="accueilBtn" to="/connect">connectez-vous</Link>
                </div>

            </main>
        </>
    )
}

export default Accueil