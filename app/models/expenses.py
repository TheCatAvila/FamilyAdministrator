from app.database.db_connection import Database

class Expense:
    def __init__(self, id: int = None, amount: float = None, description: str = None, date: str = None, subcategory_id: int = None, family_id: int = None, user_id: int = None):
        self.id = id
        self.amount = amount
        self.description = description
        self.date = date
        self.subcategory_id = subcategory_id
        self.family_id = family_id
        self.user_id = user_id

    def create(self):
        """Crea un nuevo egreso."""
        try:
            if self.description:
                print(f"Descripción: {self.description}")
                query = """INSERT INTO expenses (
                                amount, 
                                description,
                                date, 
                                subcategory_id,
                                family_id,
                                user_id,
                                register_date) 
                            VALUES (%s, %s, %s, %s, %s, %s, now())"""
                values = (self.amount, self.description, self.date, self.subcategory_id, self.family_id, self.user_id)
            else:
                query = """INSERT INTO expenses (
                                amount, 
                                date, 
                                subcategory_id,
                                family_id,
                                user_id,
                                register_date) 
                            VALUES (%s, %s, %s, %s, %s, now())"""
                values = (self.amount, self.date, self.subcategory_id, self.family_id, self.user_id)
                print("values sin descripción:", values)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Egreso creado exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
        
    def delete(self):
        """Elimina un egreso."""
        try:
            query = "DELETE FROM expenses WHERE id = %s"
            values = (self.id,)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Egreso eliminado exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def edit(self):
        """Edita un egreso."""
        try:
            query = """UPDATE expenses 
                        SET amount = %s, 
                            description = %s, 
                            date = %s, 
                            subcategory_id = %s, 
                            family_id = %s, 
                            user_id = %s
                        WHERE id = %s"""
            values = (self.amount, self.description, self.date, self.subcategory_id, self.family_id, self.user_id, self.id)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Egreso editado exitosamente."}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
    
    def get_all_by_family(self):
        """Obtiene todos los egresos de una familia."""
        try:
            query = """SELECT 
                            e.id, 
                            e.amount, 
                            e.description,
                            e.date, 
                            e.subcategory_id,
                            e.family_id,
                            e.user_id,
                            e.register_date,
                            es.name AS subcategory_name,
                            ec.name AS category_name
                        FROM 
                            expenses AS e
                        JOIN 
                            expense_subcategory AS es ON e.subcategory_id = es.id
                        JOIN 
                            expense_category AS ec ON es.category_id = ec.id
                        WHERE 
                            e.family_id = %s
                        ORDER BY 
                            e.date DESC"""
            with Database() as db:
                values = (self.family_id,)
                db.execute(query, values)
                expenses = db.fetchall()
            
            return {"success": True, "expenses": expenses}
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
        
    def get_total_expense_by_family(self):
        """Obtiene el total de egresos de una familia."""
        try:
            query = """SELECT 
                            SUM(amount) AS total_expense 
                        FROM 
                            expenses 
                        WHERE 
                            family_id = %s"""
            with Database() as db:
                values = (self.family_id,)
                db.execute(query, values)
                total_expense = db.fetchone()
            
            return {"success": True, "total_expense": total_expense['total_expense']}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}