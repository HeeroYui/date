/**
 * @author Edouard DUPIN
 * 
 * @copyright 2011, Edouard DUPIN, all right reserved
 * 
 * @license BSD v3 (see license file)
 */
#pragma once
extern "C" {
	#include <stdint.h>
}

/**
 * @brief date library namespace
 */
namespace date {
	/**
	 * @brief Get the Build year of the program
	 * @return The number of the year (ex: 2015 or 1995)
	 */
	int32_t getYear();
	/**
	 * @brief Get the Build month id
	 * @return The number of the month (ex: 1 for january or 9 for september ...)
	 */
	int32_t getMonth();
	/**
	 * @brief Get the Build day in the month
	 * @return The number of the month day [1..31]
	 */
	int32_t getDay();
	/**
	 * @brief Get the Build hour
	 * @return The number of the hour [0..23]
	 */
	int32_t getHour();
	/**
	 * @brief Get the Build Minute
	 * @return The number of the minute [0..59]
	 */
	int32_t getMinute();
	/**
	 * @brief Get the Build second
	 * @return The number of the second [0..59]
	 */
	int32_t getSecond();
};

