/* Copyright (C) 2021 Barcelona Supercomputing Center and University of
 * Illinois at Urbana-Champaign
 * SPDX-License-Identifier: MIT
 *
 * Emission reaction solver functions
 *
 */
/** \file
 * \brief Emission reaction solver functions
 */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "../rxns.h"

// TODO Lookup environmental indicies during initialization
#define TEMPERATURE_K_ env_data[0]
#define PRESSURE_PA_ env_data[1]

#define RXN_ID_ (int_data[0])
#define SPECIES_ (int_data[1] - 1)
#define DERIV_ID_ int_data[2]
#define SCALING_ float_data[0]
#define RATE_ (rxn_env_data[0])
#define BASE_RATE_ (rxn_env_data[1])
#define NUM_INT_PROP_ 3
#define NUM_FLOAT_PROP_ 1
#define NUM_ENV_PARAM_ 2

/** \brief Flag Jacobian elements used by this reaction
 *
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 * \param jac Jacobian
 */
void rxn_emission_get_used_jac_elem(int *rxn_int_data, double *rxn_float_data,
                                    Jacobian *jac) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;

  return;
}

/** \brief Update the time derivative and Jacbobian array indices
 *
 * \param model_data Pointer to the model data
 * \param deriv_ids Id of each state variable in the derivative array
 * \param jac Jacobian
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 */
void rxn_emission_update_ids(ModelData *model_data, int *deriv_ids,
                             Jacobian jac, int *rxn_int_data,
                             double *rxn_float_data) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;

  // Update the time derivative id
  DERIV_ID_ = deriv_ids[SPECIES_];

  return;
}

/** \brief Update reaction data
 *
 * Emission reactions can have their base (pre-scaling) rates updated from the
 * host model based on the calculations of an external module. The structure
 * of the update data is:
 *
 *  - \b int rxn_id (Id of one or more emission reactions set by the
 *       host model using the
 *       \c camp_rxn_emission::rxn_emission_t::set_rxn_id
 *       function prior to initializing the solver.)
 *  - \b double rate (New pre-scaling rate.)
 *
 * \param update_data Pointer to the updated reaction data
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 * \param rxn_env_data Pointer to the environment-dependent data
 * \return Flag indicating whether this is the reaction to update
 */
bool rxn_emission_update_data(void *update_data, int *rxn_int_data,
                              double *rxn_float_data, double *rxn_env_data) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;

  int *rxn_id = (int *)update_data;
  double *base_rate = (double *)&(rxn_id[1]);

  // Set the base emission rate for matching reactions
  if (*rxn_id == RXN_ID_ && RXN_ID_ > 0) {
    BASE_RATE_ = (double)*base_rate;
    RATE_ = SCALING_ * BASE_RATE_;
    return true;
  }

  return false;
}

/** \brief Update reaction data for new environmental conditions
 *
 * For emission reactions this only involves recalculating the rate.
 *
 * \param model_data Pointer to the model data
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 * \param rxn_env_data Pointer to the environment-dependent parameters
 */
void rxn_emission_update_env_state(ModelData *model_data, int *rxn_int_data,
                                   double *rxn_float_data,
                                   double *rxn_env_data) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;
  double *env_data = model_data->grid_cell_env;

  // Calculate the rate constant in (concentration_units/s)
  RATE_ = SCALING_ * BASE_RATE_;

  return;
}

/** \brief Calculate contributions to the time derivative \f$f(t,y)\f$ from
 * this reaction.
 *
 * \param model_data Pointer to the model data, including the state array
 * \param time_deriv TimeDerivative object
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 * \param rxn_env_data Pointer to the environment-dependent parameters
 * \param time_step Current time step being computed (s)
 */
#ifdef CAMP_USE_SUNDIALS
void rxn_emission_calc_deriv_contrib(ModelData *model_data,
                                     TimeDerivative time_deriv,
                                     int *rxn_int_data, double *rxn_float_data,
                                     double *rxn_env_data, realtype time_step) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;
  double *state = model_data->grid_cell_state;
  double *env_data = model_data->grid_cell_env;

  // Add contributions to the time derivative
  if (DERIV_ID_ >= 0)
    time_derivative_add_value(time_deriv, DERIV_ID_, (long double)RATE_);

  return;
}
#endif

/** \brief Calculate contributions to the Jacobian from this reaction
 *
 * \param model_data Pointer to the model data
 * \param jac Reaction Jacobian
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 * \param rxn_env_data Pointer to the environment-dependent parameters
 * \param time_step Current time step being calculated (s)
 */
#ifdef CAMP_USE_SUNDIALS
void rxn_emission_calc_jac_contrib(ModelData *model_data, Jacobian jac,
                                   int *rxn_int_data, double *rxn_float_data,
                                   double *rxn_env_data, realtype time_step) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;
  double *state = model_data->grid_cell_state;
  double *env_data = model_data->grid_cell_env;

  // No Jacobian contributions from 0th order emissions

  return;
}
#endif

/** \brief Print the reaction parameters
 *
 * \param rxn_int_data Pointer to the reaction integer data
 * \param rxn_float_data Pointer to the reaction floating-point data
 */
void rxn_emission_print(int *rxn_int_data, double *rxn_float_data) {
  int *int_data = rxn_int_data;
  double *float_data = rxn_float_data;

  printf("\n\nEmission reaction\n");

  return;
}

/** \brief Create update data for new emission rates
 *
 * \return Pointer to a new rate update data object
 */
void *rxn_emission_create_rate_update_data() {
  int *update_data = (int *)malloc(sizeof(int) + sizeof(double));
  if (update_data == NULL) {
    printf("\n\nERROR allocating space for emission update data\n\n");
    exit(1);
  }
  return (void *)update_data;
}

/** \brief Set rate update data
 *
 * \param update_data Pointer to an allocated rate update data object
 * \param rxn_id Id of emission reactions to update
 * \param base_rate New pre-scaling emission rate
 */
void rxn_emission_set_rate_update_data(void *update_data, int rxn_id,
                                       double base_rate) {
  int *new_rxn_id = (int *)update_data;
  double *new_base_rate = (double *)&(new_rxn_id[1]);
  *new_rxn_id = rxn_id;
  *new_base_rate = base_rate;
}
