/***************************************************************************/
/*
 * Ani.c
 *
 * Warzone animation function wrappers
 *
 * Gareth Jones 16/12/97
 */
/***************************************************************************/

#include "lib/gamelib/ani.h"

/***************************************************************************/

void *
anim_GetShapeFunc( STRING * pStr )
{
	return resGetData( "IMD", pStr );
}

/***************************************************************************/
