import { useState } from "react"
import NavbarPartenaire from "../utils/navBarre"
import axios from "axios"


const AccueilPartenaire = () => {

    const [nomProduit, setNomProduit] = useState('')
    const [descriptionProduit, setDescriptionProduit] = useState('')
    const [prixProduit, setPrixProduit] = useState('')
    const [imageProduit, setImageProduit] = useState('')
    const [categorie, setCategorie] = useState('')

    const handleProductName = (e) => {
        setNomProduit(e.target.value)
    }

    const handleProductDes = (e) => {
        setDescriptionProduit(e.target.value)
    } 

    const handleProductPrice = (e) => {
        setPrixProduit(e.target.value)
    }

    const handleProductImage = (e) => {
        setImageProduit(e.target.value)
    }

    const handleProductCategorie = (e) => {
        setCategorie(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(nomProduit,  descriptionProduit, prixProduit, imageProduit, categorie)

        axios.post('http://localhost:3001/api/auth/ajoutproduit', {
            nomProduit: nomProduit,
            descriptionProduit: descriptionProduit,
            prixProduit: prixProduit,
            imageProduit: imageProduit,
            categorieProduit: categorie
        }).then(res => {
            console.log(res.data)
            setCategorie('')
            setDescriptionProduit('')
            setImageProduit('')
            setNomProduit('')
            setPrixProduit('')
        }).catch(err => {
            console.log('Encore une erreur', err)
        })

        



    }


    return(
        <>
            <NavbarPartenaire />

            <div className="ajouterProduit">
                <div className="card-ajouter-produit">
                    <h2>Ajouter un produit</h2>
                    <form onSubmit={handleSubmit}>
                        <div className="nom-produit">
                            <label htmlFor="nom-produit">Nom du produit</label>
                            <input type="text" id="nom-produit" name="nomProduit" value={nomProduit} onChange={handleProductName} required />
                        </div>
                        <div className="description-produit">
                            <label htmlFor="description-produit">Description</label>
                            <textarea id="description-produit" name="descriptionProduit" value={descriptionProduit} onChange={handleProductDes} rows="3" required></textarea>
                        </div>
                        <div className="prix-produit">
                            <label htmlFor="prix-produit">Prix</label>
                            <input type="number" id="prix-produit" name="prixProduit" min="0" value={prixProduit} onChange={handleProductPrice} step="1" required />
                        </div>
                        <div className="categorie-produit">
                            <label htmlFor="categorie-produit">Catégorie</label>
                            <select id="categorie-produit" name="categorieProduit" value={categorie} onChange={handleProductCategorie} required>
                                <option value="">Sélectionnez une catégorie</option>
                                <option value="electronique">Électronique</option>
                                <option value="informatique">Informatique</option>
                                <option value="telephonie">Téléphonie</option>
                            </select>
                        </div>
                        <div className="image-produit">
                            <label htmlFor="image-produit">Image du produit</label>
                            <input type="file" id="image-produit" name="imageProduit" accept="image/*" value={imageProduit} onChange={handleProductImage} required />
                        </div>
                        <div className="btn">
                            <button type="submit">Ajouter le produit</button>
                        </div>
                    </form>
                </div>
            </div>
        </>
    )
}

export default AccueilPartenaire