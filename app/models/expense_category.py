from app.database.db_connection import Database

class ExpenseCategory:
    def __init__(self, id: int = None, name: str = None, family_id: int = None):
        self.id = id
        self.name = name
        self.family_id = family_id
    
    def get_all_of_family(self):
        """Obtiene todas las categorías de egresos."""
        try:
            query = """SELECT 
                            ec.id, 
                            ec.name, 
                            SUM(es.budget) AS total_category_budget
                        FROM 
                            expense_category ec
                        LEFT JOIN 
                            expense_subcategory es ON ec.id = es.category_id
						WHERE 
							family_id = %s
                        GROUP BY 
                            ec.id, ec.name
                        ORDER BY 
                            name ASC;
                    """
            with Database() as db:
                values = (self.family_id,)
                db.execute(query, values)
                categories = db.fetchall()
            
            return {"success": True, "categories": categories}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_select_data(self):
        """Obtiene los nombres de todas las categorías de egresos."""
        try:
            query = """SELECT 
                            id, name 
                        FROM 
                            expense_category
                        WHERE
                            family_id = %s
                        ORDER BY 
                            name ASC
                    """
            with Database() as db:
                values = (self.family_id,)
                db.execute(query, values)
                categories = db.fetchall()
            
            return {"success": True, "categories": categories}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_id_by_name(self):
        """Obtiene el ID de una categoría de egresos por su nombre."""
        try:
            query = "SELECT id FROM expense_category WHERE name = %s"
            values = (self.name,)
            with Database() as db:
                db.execute(query, values)
                category_id = db.fetchone()
            
            if category_id:
                return {"success": True, "id": category_id['id']}
            else:
                return {"success": False, "error": "Categoría no encontrada."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}

    def create(self):
        """Crea una nueva categoría de egresos."""
        try:
            query = "INSERT INTO expense_category (name, family_id) VALUES (%s, %s)"
            values = (self.name, self.family_id)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Categoría creada exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}