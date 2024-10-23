import { Link } from "react-router-dom"
import Navbar from "../utils/navBarre"
import loupe from "../Assets/chercher.png"
import Produit from "./Produits"
import security from "../Assets/security.png"
import multitude from "../Assets/multitude.png"
import carte from "../Assets/carte.png"
import experience from "../Assets/experience.png"

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

                <div className="secondMain">
                    <div className="item">
                        <div className="roundBox">
                            <img src={security} alt="" />
                        </div>
                        <h2>Qualité des articles</h2>
                        <p>Nous mettons à votre disposition des articles de super bonnes qualités</p>
                    </div>
                    <div className="item">
                        <div className="roundBox">
                            <img src={multitude} alt="" />
                        </div>
                        <h2>Plusieurs articles pour vous</h2>
                        <p>
                            Nous avons ici des multitudes d'articles électroménagers en notre sein
                        </p>
                    </div>
                    <div className="item">
                        <div className="roundBox">
                            <img src={carte} alt="" />
                        </div>
                        <h2>Payez à credit</h2>
                        <p>Vous pouvez prendre des articles et decider de les payer plus tard</p>
                    </div>
                    <div className="item">
                        <div className="roundBox">
                            <img src={experience} alt="" />
                        </div>
                        <h2>Experience sur mesure</h2>
                        <p>Beneficiez des plusieurs offres telles que les reductions sur articles, les assistances et autres</p>
                    </div>
                </div>

            </main>
        </>
    )
}

export default Accueil