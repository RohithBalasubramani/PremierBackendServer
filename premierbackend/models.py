# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllInvGenNew(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    today_inv1 = models.FloatField(db_column='TODAY_INV1', blank=True, null=True)  # Field name made lowercase.
    total_inv1 = models.FloatField(db_column='TOTAL_INV1', blank=True, null=True)  # Field name made lowercase.
    today_inv10 = models.FloatField(db_column='TODAY_INV10', blank=True, null=True)  # Field name made lowercase.
    total_inv10 = models.FloatField(db_column='TOTAL_INV10', blank=True, null=True)  # Field name made lowercase.
    today_inv11 = models.FloatField(db_column='TODAY_INV11', blank=True, null=True)  # Field name made lowercase.
    total_inv11 = models.FloatField(db_column='TOTAL_INV11', blank=True, null=True)  # Field name made lowercase.
    today_inv12 = models.FloatField(db_column='TODAY_INV12', blank=True, null=True)  # Field name made lowercase.
    total_inv12 = models.FloatField(db_column='TOTAL_INV12', blank=True, null=True)  # Field name made lowercase.
    today_inv13 = models.FloatField(db_column='TODAY_INV13', blank=True, null=True)  # Field name made lowercase.
    total_inv13 = models.FloatField(db_column='TOTAL_INV13', blank=True, null=True)  # Field name made lowercase.
    today_inv14 = models.FloatField(db_column='TODAY_INV14', blank=True, null=True)  # Field name made lowercase.
    total_inv14 = models.FloatField(db_column='TOTAL_INV14', blank=True, null=True)  # Field name made lowercase.
    today_inv15 = models.FloatField(db_column='TODAY_INV15', blank=True, null=True)  # Field name made lowercase.
    total_inv15 = models.FloatField(db_column='TOTAL_INV15', blank=True, null=True)  # Field name made lowercase.
    today_inv16 = models.FloatField(db_column='TODAY_INV16', blank=True, null=True)  # Field name made lowercase.
    total_inv16 = models.FloatField(db_column='TOTAL_INV16', blank=True, null=True)  # Field name made lowercase.
    today_inv17 = models.FloatField(db_column='TODAY_INV17', blank=True, null=True)  # Field name made lowercase.
    total_inv17 = models.FloatField(db_column='TOTAL_INV17', blank=True, null=True)  # Field name made lowercase.
    today_inv18 = models.FloatField(db_column='TODAY_INV18', blank=True, null=True)  # Field name made lowercase.
    total_inv18 = models.FloatField(db_column='TOTAL_INV18', blank=True, null=True)  # Field name made lowercase.
    today_inv19 = models.FloatField(db_column='TODAY_INV19', blank=True, null=True)  # Field name made lowercase.
    total_inv19 = models.FloatField(db_column='TOTAL_INV19', blank=True, null=True)  # Field name made lowercase.
    today_inv2 = models.FloatField(db_column='TODAY_INV2', blank=True, null=True)  # Field name made lowercase.
    total_inv2 = models.FloatField(db_column='TOTAL_INV2', blank=True, null=True)  # Field name made lowercase.
    today_inv20 = models.FloatField(db_column='TODAY_INV20', blank=True, null=True)  # Field name made lowercase.
    total_inv20 = models.FloatField(db_column='TOTAL_INV20', blank=True, null=True)  # Field name made lowercase.
    today_inv21 = models.FloatField(db_column='TODAY_INV21', blank=True, null=True)  # Field name made lowercase.
    total_inv21 = models.FloatField(db_column='TOTAL_INV21', blank=True, null=True)  # Field name made lowercase.
    today_inv22 = models.FloatField(db_column='TODAY_INV22', blank=True, null=True)  # Field name made lowercase.
    total_inv22 = models.FloatField(db_column='TOTAL_INV22', blank=True, null=True)  # Field name made lowercase.
    today_inv23 = models.FloatField(db_column='TODAY_INV23', blank=True, null=True)  # Field name made lowercase.
    total_inv23 = models.FloatField(db_column='TOTAL_INV23', blank=True, null=True)  # Field name made lowercase.
    today_inv24 = models.FloatField(db_column='TODAY_INV24', blank=True, null=True)  # Field name made lowercase.
    total_inv24 = models.FloatField(db_column='TOTAL_INV24', blank=True, null=True)  # Field name made lowercase.
    today_inv25 = models.FloatField(db_column='TODAY_INV25', blank=True, null=True)  # Field name made lowercase.
    total_inv25 = models.FloatField(db_column='TOTAL_INV25', blank=True, null=True)  # Field name made lowercase.
    today_inv26 = models.FloatField(db_column='TODAY_INV26', blank=True, null=True)  # Field name made lowercase.
    total_inv26 = models.FloatField(db_column='TOTAL_INV26', blank=True, null=True)  # Field name made lowercase.
    today_inv27 = models.FloatField(db_column='TODAY_INV27', blank=True, null=True)  # Field name made lowercase.
    total_inv27 = models.FloatField(db_column='TOTAL_INV27', blank=True, null=True)  # Field name made lowercase.
    today_inv28 = models.FloatField(db_column='TODAY_INV28', blank=True, null=True)  # Field name made lowercase.
    total_inv28 = models.FloatField(db_column='TOTAL_INV28', blank=True, null=True)  # Field name made lowercase.
    today_inv29 = models.FloatField(db_column='TODAY_INV29', blank=True, null=True)  # Field name made lowercase.
    total_inv29 = models.FloatField(db_column='TOTAL_INV29', blank=True, null=True)  # Field name made lowercase.
    today_inv3 = models.FloatField(db_column='TODAY_INV3', blank=True, null=True)  # Field name made lowercase.
    total_inv3 = models.FloatField(db_column='TOTAL_INV3', blank=True, null=True)  # Field name made lowercase.
    today_inv30 = models.FloatField(db_column='TODAY_INV30', blank=True, null=True)  # Field name made lowercase.
    total_inv30 = models.FloatField(db_column='TOTAL_INV30', blank=True, null=True)  # Field name made lowercase.
    today_inv31 = models.FloatField(db_column='TODAY_INV31', blank=True, null=True)  # Field name made lowercase.
    total_inv31 = models.FloatField(db_column='TOTAL_INV31', blank=True, null=True)  # Field name made lowercase.
    today_inv32 = models.FloatField(db_column='TODAY_INV32', blank=True, null=True)  # Field name made lowercase.
    total_inv32 = models.FloatField(db_column='TOTAL_INV32', blank=True, null=True)  # Field name made lowercase.
    today_inv33 = models.FloatField(db_column='TODAY_INV33', blank=True, null=True)  # Field name made lowercase.
    total_inv33 = models.FloatField(db_column='TOTAL_INV33', blank=True, null=True)  # Field name made lowercase.
    today_inv34 = models.FloatField(db_column='TODAY_INV34', blank=True, null=True)  # Field name made lowercase.
    total_inv34 = models.FloatField(db_column='TOTAL_INV34', blank=True, null=True)  # Field name made lowercase.
    today_inv35 = models.FloatField(db_column='TODAY_INV35', blank=True, null=True)  # Field name made lowercase.
    total_inv35 = models.FloatField(db_column='TOTAL_INV35', blank=True, null=True)  # Field name made lowercase.
    today_inv36 = models.FloatField(db_column='TODAY_INV36', blank=True, null=True)  # Field name made lowercase.
    total_inv36 = models.FloatField(db_column='TOTAL_INV36', blank=True, null=True)  # Field name made lowercase.
    today_inv37 = models.FloatField(db_column='TODAY_INV37', blank=True, null=True)  # Field name made lowercase.
    total_inv37 = models.FloatField(db_column='TOTAL_INV37', blank=True, null=True)  # Field name made lowercase.
    today_inv38 = models.FloatField(db_column='TODAY_INV38', blank=True, null=True)  # Field name made lowercase.
    total_inv38 = models.FloatField(db_column='TOTAL_INV38', blank=True, null=True)  # Field name made lowercase.
    today_inv4 = models.FloatField(db_column='TODAY_INV4', blank=True, null=True)  # Field name made lowercase.
    total_inv4 = models.FloatField(db_column='TOTAL_INV4', blank=True, null=True)  # Field name made lowercase.
    today_inv5 = models.FloatField(db_column='TODAY_INV5', blank=True, null=True)  # Field name made lowercase.
    total_inv5 = models.FloatField(db_column='TOTAL_INV5', blank=True, null=True)  # Field name made lowercase.
    today_inv6 = models.FloatField(db_column='TODAY_INV6', blank=True, null=True)  # Field name made lowercase.
    total_inv6 = models.FloatField(db_column='TOTAL_INV6', blank=True, null=True)  # Field name made lowercase.
    today_inv7 = models.FloatField(db_column='TODAY_INV7', blank=True, null=True)  # Field name made lowercase.
    total_inv7 = models.FloatField(db_column='TOTAL_INV7', blank=True, null=True)  # Field name made lowercase.
    today_inv8 = models.FloatField(db_column='TODAY_INV8', blank=True, null=True)  # Field name made lowercase.
    total_inv8 = models.FloatField(db_column='TOTAL_INV8', blank=True, null=True)  # Field name made lowercase.
    today_inv9 = models.FloatField(db_column='TODAY_INV9', blank=True, null=True)  # Field name made lowercase.
    total_inv9 = models.FloatField(db_column='TOTAL_INV9', blank=True, null=True)  # Field name made lowercase.
    yest_inv_1 = models.FloatField(db_column='YEST_INV_1', blank=True, null=True)  # Field name made lowercase.
    yest_inv_10 = models.FloatField(db_column='YEST_INV_10', blank=True, null=True)  # Field name made lowercase.
    yest_inv_11 = models.FloatField(db_column='YEST_INV_11', blank=True, null=True)  # Field name made lowercase.
    yest_inv_12 = models.FloatField(db_column='YEST_INV_12', blank=True, null=True)  # Field name made lowercase.
    yest_inv_13 = models.FloatField(db_column='YEST_INV_13', blank=True, null=True)  # Field name made lowercase.
    yest_inv_14 = models.FloatField(db_column='YEST_INV_14', blank=True, null=True)  # Field name made lowercase.
    yest_inv_15 = models.FloatField(db_column='YEST_INV_15', blank=True, null=True)  # Field name made lowercase.
    yest_inv_16 = models.FloatField(db_column='YEST_INV_16', blank=True, null=True)  # Field name made lowercase.
    yest_inv_17 = models.FloatField(db_column='YEST_INV_17', blank=True, null=True)  # Field name made lowercase.
    yest_inv_18 = models.FloatField(db_column='YEST_INV_18', blank=True, null=True)  # Field name made lowercase.
    yest_inv_19 = models.FloatField(db_column='YEST_INV_19', blank=True, null=True)  # Field name made lowercase.
    yest_inv_2 = models.FloatField(db_column='YEST_INV_2', blank=True, null=True)  # Field name made lowercase.
    yest_inv_20 = models.FloatField(db_column='YEST_INV_20', blank=True, null=True)  # Field name made lowercase.
    yest_inv_21 = models.FloatField(db_column='YEST_INV_21', blank=True, null=True)  # Field name made lowercase.
    yest_inv_22 = models.FloatField(db_column='YEST_INV_22', blank=True, null=True)  # Field name made lowercase.
    yest_inv_23 = models.FloatField(db_column='YEST_INV_23', blank=True, null=True)  # Field name made lowercase.
    yest_inv_24 = models.FloatField(db_column='YEST_INV_24', blank=True, null=True)  # Field name made lowercase.
    yest_inv_25 = models.FloatField(db_column='YEST_INV_25', blank=True, null=True)  # Field name made lowercase.
    yest_inv_26 = models.FloatField(db_column='YEST_INV_26', blank=True, null=True)  # Field name made lowercase.
    yest_inv_27 = models.FloatField(db_column='YEST_INV_27', blank=True, null=True)  # Field name made lowercase.
    yest_inv_28 = models.FloatField(db_column='YEST_INV_28', blank=True, null=True)  # Field name made lowercase.
    yest_inv_29 = models.FloatField(db_column='YEST_INV_29', blank=True, null=True)  # Field name made lowercase.
    yest_inv_3 = models.FloatField(db_column='YEST_INV_3', blank=True, null=True)  # Field name made lowercase.
    yest_inv_30 = models.FloatField(db_column='YEST_INV_30', blank=True, null=True)  # Field name made lowercase.
    yest_inv_31 = models.FloatField(db_column='YEST_INV_31', blank=True, null=True)  # Field name made lowercase.
    yest_inv_32 = models.FloatField(db_column='YEST_INV_32', blank=True, null=True)  # Field name made lowercase.
    yest_inv_33 = models.FloatField(db_column='YEST_INV_33', blank=True, null=True)  # Field name made lowercase.
    yest_inv_34 = models.FloatField(db_column='YEST_INV_34', blank=True, null=True)  # Field name made lowercase.
    yest_inv_35 = models.FloatField(db_column='YEST_INV_35', blank=True, null=True)  # Field name made lowercase.
    yest_inv_36 = models.FloatField(db_column='YEST_INV_36', blank=True, null=True)  # Field name made lowercase.
    yest_inv_37 = models.FloatField(db_column='YEST_INV_37', blank=True, null=True)  # Field name made lowercase.
    yest_inv_38 = models.FloatField(db_column='YEST_INV_38', blank=True, null=True)  # Field name made lowercase.
    yest_inv_4 = models.FloatField(db_column='YEST_INV_4', blank=True, null=True)  # Field name made lowercase.
    yest_inv_5 = models.FloatField(db_column='YEST_INV_5', blank=True, null=True)  # Field name made lowercase.
    yest_inv_6 = models.FloatField(db_column='YEST_INV_6', blank=True, null=True)  # Field name made lowercase.
    yest_inv_7 = models.FloatField(db_column='YEST_INV_7', blank=True, null=True)  # Field name made lowercase.
    yest_inv_8 = models.FloatField(db_column='YEST_INV_8', blank=True, null=True)  # Field name made lowercase.
    yest_inv_9 = models.FloatField(db_column='YEST_INV_9', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALL_INV_GEN_NEW'


class AmfHtMfm9(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_HT_MFM_9'


class AmfMfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_1'


class AmfMfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_2'


class AmfMfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_3'


class AmfMfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_4'


class AmfMfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_5'


class AmfMfm6(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_6'


class AmfMfm7(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_7'


class AmfMfm8(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMF_MFM_8'


class Cell1HtMfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_HT_MFM_1'


class Cell1HtMfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_HT_MFM_2'


class Cell1HtMfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_HT_MFM_3'


class Cell1HtMfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_HT_MFM_4'


class Cell1HtMfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_HT_MFM_5'


class Cell1Mfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_1'


class Cell1Mfm10(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_10'


class Cell1Mfm11(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_11'


class Cell1Mfm12(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_12'


class Cell1Mfm13(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_13'


class Cell1Mfm14(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_14'


class Cell1Mfm15(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_15'


class Cell1Mfm16(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_16'


class Cell1Mfm17(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_17'


class Cell1Mfm18(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_18'


class Cell1Mfm19(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_19'


class Cell1Mfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_2'


class Cell1Mfm20(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_20'


class Cell1Mfm21(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_21'


class Cell1Mfm22(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_22'


class Cell1Mfm23(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_23'


class Cell1Mfm24(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_24'


class Cell1Mfm25(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_25'


class Cell1Mfm26(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_26'


class Cell1Mfm27(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_27'


class Cell1Mfm28(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_28'


class Cell1Mfm29(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_29'


class Cell1Mfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_3'


class Cell1Mfm30(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_30'


class Cell1Mfm31(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_31'


class Cell1Mfm32(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_32'


class Cell1Mfm33(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_33'


class Cell1Mfm34(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_34'


class Cell1Mfm35(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_35'


class Cell1Mfm36(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_36'


class Cell1Mfm37(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_37'


class Cell1Mfm38(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_38'


class Cell1Mfm39(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_39'


class Cell1Mfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_4'


class Cell1Mfm40(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_40'


class Cell1Mfm41(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_41'


class Cell1Mfm42(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_42'


class Cell1Mfm43(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_43'


class Cell1Mfm44(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_44'


class Cell1Mfm45(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_45'


class Cell1Mfm46(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_46'


class Cell1Mfm47(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_47'


class Cell1Mfm48(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_48'


class Cell1Mfm49(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_49'


class Cell1Mfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_5'


class Cell1Mfm50(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_50'


class Cell1Mfm51(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_51'


class Cell1Mfm52(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_52'


class Cell1Mfm53(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_53'


class Cell1Mfm54(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_54'


class Cell1Mfm55(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_55'


class Cell1Mfm56(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_56'


class Cell1Mfm57(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_57'


class Cell1Mfm58(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_58'


class Cell1Mfm59(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_59'


class Cell1Mfm6(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_6'


class Cell1Mfm60(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_60'


class Cell1Mfm61(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_61'


class Cell1Mfm62(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_62'


class Cell1Mfm63(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_63'


class Cell1Mfm64(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_64'


class Cell1Mfm65(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_65'


class Cell1Mfm66(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_66'


class Cell1Mfm67(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_67'


class Cell1Mfm68(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_68'


class Cell1Mfm69(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_69'


class Cell1Mfm7(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_7'


class Cell1Mfm70(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_70'


class Cell1Mfm8(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_8'


class Cell1Mfm9(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_1_MFM_9'


class Cell2Mfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_1'


class Cell2Mfm10(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_10'


class Cell2Mfm11(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_11'


class Cell2Mfm12(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_12'


class Cell2Mfm13(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_13'


class Cell2Mfm14(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_14'


class Cell2Mfm15(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_15'


class Cell2Mfm16(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_16'


class Cell2Mfm17(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_17'


class Cell2Mfm18(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_18'


class Cell2Mfm19(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_19'


class Cell2Mfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_2'


class Cell2Mfm20(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_20'


class Cell2Mfm21(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_21'


class Cell2Mfm22(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_22'


class Cell2Mfm23(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_23'


class Cell2Mfm24(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_24'


class Cell2Mfm25(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_25'


class Cell2Mfm26(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_26'


class Cell2Mfm27(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_27'


class Cell2Mfm28(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_28'


class Cell2Mfm29(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_29'


class Cell2Mfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_3'


class Cell2Mfm30(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_30'


class Cell2Mfm31(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_31'


class Cell2Mfm32(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_32'


class Cell2Mfm33(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_33'


class Cell2Mfm34(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_34'


class Cell2Mfm35(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_35'


class Cell2Mfm36(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_36'


class Cell2Mfm37(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_37'


class Cell2Mfm38(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_38'


class Cell2Mfm39(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_39'


class Cell2Mfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_4'


class Cell2Mfm40(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_40'


class Cell2Mfm41(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_41'


class Cell2Mfm42(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_42'


class Cell2Mfm43(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_43'


class Cell2Mfm44(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_44'


class Cell2Mfm45(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_45'


class Cell2Mfm46(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_46'


class Cell2Mfm47(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_47'


class Cell2Mfm48(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_48'


class Cell2Mfm49(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_49'


class Cell2Mfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_5'


class Cell2Mfm50(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_50'


class Cell2Mfm51(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_51'


class Cell2Mfm52(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_52'


class Cell2Mfm53(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_53'


class Cell2Mfm6(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_6'


class Cell2Mfm7(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_7'


class Cell2Mfm8(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_8'


class Cell2Mfm9(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CELL_2_MFM_9'


class Drivers(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventcol = models.CharField(db_column='EventCol', max_length=24, blank=True, null=True)  # Field name made lowercase.
    evnumcol = models.SmallIntegerField(db_column='EvNumCol', blank=True, null=True)  # Field name made lowercase.
    evdesccol = models.CharField(db_column='EvDescCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desccol = models.CharField(db_column='DescCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commcol = models.CharField(db_column='CommCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durcol = models.IntegerField(db_column='DurCol', blank=True, null=True)  # Field name made lowercase.
    uniid = models.IntegerField(db_column='UniID', blank=True, null=True)  # Field name made lowercase.
    traid = models.IntegerField(db_column='TraID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Drivers'


class Ht2Mfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HT2_MFM1'


class Ht2Mfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HT2_MFM2'


class Ht2Mfm21(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HT2_MFM21'


class Ht2Mfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HT2_MFM3'


class Ht2Mfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HT2_MFM4'


class Ht2Mfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_power_factor = models.FloatField(db_column='AVG_POWER_FACTOR', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_appernt_energy = models.FloatField(db_column='TODAY_APPERNT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    today_gen = models.FloatField(db_column='TODAY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_apparent_energy = models.FloatField(db_column='TOTAL_APPARENT_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HT2_MFM5'


class InvertersActiveCurrent(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_2 = models.FloatField(db_column='INV_2', blank=True, null=True)  # Field name made lowercase.
    inv_1 = models.FloatField(db_column='INV_1', blank=True, null=True)  # Field name made lowercase.
    inv_3 = models.FloatField(db_column='INV_3', blank=True, null=True)  # Field name made lowercase.
    inv_4 = models.FloatField(db_column='INV_4', blank=True, null=True)  # Field name made lowercase.
    inv_5 = models.FloatField(db_column='INV_5', blank=True, null=True)  # Field name made lowercase.
    inv_6 = models.FloatField(db_column='INV_6', blank=True, null=True)  # Field name made lowercase.
    inv_7 = models.FloatField(db_column='INV_7', blank=True, null=True)  # Field name made lowercase.
    inv_8 = models.FloatField(db_column='INV_8', blank=True, null=True)  # Field name made lowercase.
    inv_9 = models.FloatField(db_column='INV_9', blank=True, null=True)  # Field name made lowercase.
    inv_10 = models.FloatField(db_column='INV_10', blank=True, null=True)  # Field name made lowercase.
    inv_11 = models.FloatField(db_column='INV_11', blank=True, null=True)  # Field name made lowercase.
    inv_12 = models.FloatField(db_column='INV_12', blank=True, null=True)  # Field name made lowercase.
    inv_13 = models.FloatField(db_column='INV_13', blank=True, null=True)  # Field name made lowercase.
    inv_14 = models.FloatField(db_column='INV_14', blank=True, null=True)  # Field name made lowercase.
    inv_15 = models.FloatField(db_column='INV_15', blank=True, null=True)  # Field name made lowercase.
    inv_16 = models.FloatField(db_column='INV_16', blank=True, null=True)  # Field name made lowercase.
    inv_17 = models.FloatField(db_column='INV_17', blank=True, null=True)  # Field name made lowercase.
    inv_18 = models.FloatField(db_column='INV_18', blank=True, null=True)  # Field name made lowercase.
    inv_19 = models.FloatField(db_column='INV_19', blank=True, null=True)  # Field name made lowercase.
    inv_20 = models.FloatField(db_column='INV_20', blank=True, null=True)  # Field name made lowercase.
    inv_21 = models.FloatField(db_column='INV_21', blank=True, null=True)  # Field name made lowercase.
    inv_22 = models.FloatField(db_column='INV_22', blank=True, null=True)  # Field name made lowercase.
    inv_23 = models.FloatField(db_column='INV_23', blank=True, null=True)  # Field name made lowercase.
    inv_24 = models.FloatField(db_column='INV_24', blank=True, null=True)  # Field name made lowercase.
    inv_25 = models.FloatField(db_column='INV_25', blank=True, null=True)  # Field name made lowercase.
    inv_26 = models.FloatField(db_column='INV_26', blank=True, null=True)  # Field name made lowercase.
    inv_27 = models.FloatField(db_column='INV_27', blank=True, null=True)  # Field name made lowercase.
    inv_28 = models.FloatField(db_column='INV_28', blank=True, null=True)  # Field name made lowercase.
    inv_29 = models.FloatField(db_column='INV_29', blank=True, null=True)  # Field name made lowercase.
    inv_30 = models.FloatField(db_column='INV_30', blank=True, null=True)  # Field name made lowercase.
    inv_31 = models.FloatField(db_column='INV_31', blank=True, null=True)  # Field name made lowercase.
    inv_32 = models.FloatField(db_column='INV_32', blank=True, null=True)  # Field name made lowercase.
    inv_33 = models.FloatField(db_column='INV_33', blank=True, null=True)  # Field name made lowercase.
    inv_34 = models.FloatField(db_column='INV_34', blank=True, null=True)  # Field name made lowercase.
    inv_35 = models.FloatField(db_column='INV_35', blank=True, null=True)  # Field name made lowercase.
    inv_36 = models.FloatField(db_column='INV_36', blank=True, null=True)  # Field name made lowercase.
    inv_37 = models.FloatField(db_column='INV_37', blank=True, null=True)  # Field name made lowercase.
    inv_38 = models.FloatField(db_column='INV_38', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTERS _ACTIVE_CURRENT'


class Inverter1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_1'


class Inverter10(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_10'


class Inverter11(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_11'


class Inverter12(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_12'


class Inverter13(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_13'


class Inverter14(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_14'


class Inverter15(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_15'


class Inverter16(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_16'


class Inverter17(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_17'


class Inverter18(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_18'


class Inverter19(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_19'


class Inverter2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_2'


class Inverter20(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_20'


class Inverter21(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_21'


class Inverter22(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_22'


class Inverter23(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_23'


class Inverter24(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_24'


class Inverter25(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_25'


class Inverter26(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_26'


class Inverter27(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_27'


class Inverter28(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_28'


class Inverter29(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_29'


class Inverter3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_3'


class Inverter30(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_30'


class Inverter31(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_31'


class Inverter32(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_32'


class Inverter33(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_33'


class Inverter34(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_34'


class Inverter35(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_35'


class Inverter36(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_36'


class Inverter37(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_37'


class Inverter38(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_38'


class Inverter4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_4'


class Inverter5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_5'


class Inverter6(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_6'


class Inverter7(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_7'


class Inverter8(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_8'


class Inverter9(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ac_power = models.FloatField(db_column='AC_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_vtg = models.FloatField(db_column='B_VTG', blank=True, null=True)  # Field name made lowercase.
    br_vtg = models.FloatField(db_column='BR_VTG', blank=True, null=True)  # Field name made lowercase.
    dc_power = models.FloatField(db_column='DC_POWER', blank=True, null=True)  # Field name made lowercase.
    monthly = models.FloatField(db_column='MONTHLY', blank=True, null=True)  # Field name made lowercase.
    peak_ac_power = models.FloatField(db_column='PEAK_AC_POWER', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_vtg = models.FloatField(db_column='R_VTG', blank=True, null=True)  # Field name made lowercase.
    rec_power = models.FloatField(db_column='REC_POWER', blank=True, null=True)  # Field name made lowercase.
    ry_vtg = models.FloatField(db_column='RY_VTG', blank=True, null=True)  # Field name made lowercase.
    string1 = models.FloatField(db_column='STRING1', blank=True, null=True)  # Field name made lowercase.
    string10 = models.FloatField(db_column='STRING10', blank=True, null=True)  # Field name made lowercase.
    string11 = models.FloatField(db_column='STRING11', blank=True, null=True)  # Field name made lowercase.
    string12 = models.FloatField(db_column='STRING12', blank=True, null=True)  # Field name made lowercase.
    string13 = models.FloatField(db_column='STRING13', blank=True, null=True)  # Field name made lowercase.
    string14 = models.FloatField(db_column='STRING14', blank=True, null=True)  # Field name made lowercase.
    string15 = models.FloatField(db_column='STRING15', blank=True, null=True)  # Field name made lowercase.
    string16 = models.FloatField(db_column='STRING16', blank=True, null=True)  # Field name made lowercase.
    string2 = models.FloatField(db_column='STRING2', blank=True, null=True)  # Field name made lowercase.
    string3 = models.FloatField(db_column='STRING3', blank=True, null=True)  # Field name made lowercase.
    string4 = models.FloatField(db_column='STRING4', blank=True, null=True)  # Field name made lowercase.
    string5 = models.FloatField(db_column='STRING5', blank=True, null=True)  # Field name made lowercase.
    string6 = models.FloatField(db_column='STRING6', blank=True, null=True)  # Field name made lowercase.
    string7 = models.FloatField(db_column='STRING7', blank=True, null=True)  # Field name made lowercase.
    string8 = models.FloatField(db_column='STRING8', blank=True, null=True)  # Field name made lowercase.
    string9 = models.FloatField(db_column='STRING9', blank=True, null=True)  # Field name made lowercase.
    today = models.FloatField(db_column='TODAY', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_vtg = models.FloatField(db_column='Y_VTG', blank=True, null=True)  # Field name made lowercase.
    yb_vtg = models.FloatField(db_column='YB_VTG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVERTER_9'


class MdMfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM1'


class MdMfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_1'


class MdMfm10(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_10'


class MdMfm11(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_11'


class MdMfm12(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_12'


class MdMfm13(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_13'


class MdMfm14(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_14'


class MdMfm15(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_15'


class MdMfm16(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_16'


class MdMfm17(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_17'


class MdMfm18(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_18'


class MdMfm19(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_19'


class MdMfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_2'


class MdMfm20(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_20'


class MdMfm21(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_21'


class MdMfm22(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_22'


class MdMfm23(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_23'


class MdMfm24(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_24'


class MdMfm25(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_25'


class MdMfm26(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_26'


class MdMfm27(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_27'


class MdMfm28(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_28'


class MdMfm29(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_29'


class MdMfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_3'


class MdMfm30(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_30'


class MdMfm31(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_31'


class MdMfm32(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_32'


class MdMfm33(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_33'


class MdMfm34(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_34'


class MdMfm35(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_35'


class MdMfm36(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_36'


class MdMfm37(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_37'


class MdMfm38(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_38'


class MdMfm39(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_39'


class MdMfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_4'


class MdMfm40(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_40'


class MdMfm41(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_41'


class MdMfm42(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_42'


class MdMfm43(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_43'


class MdMfm44(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_44'


class MdMfm45(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_45'


class MdMfm46(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_46'


class MdMfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_5'


class MdMfm6(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_6'


class MdMfm7(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_7'


class MdMfm8(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_8'


class MdMfm9(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    mfm_name = models.CharField(db_column='MFM_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfm = models.CharField(db_column='MFM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MD_MFM_9'


class Mfm1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_1'


class Mfm10(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_10'


class Mfm11(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_11'


class Mfm12(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_12'


class Mfm13(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_13'


class Mfm14(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_14'


class Mfm15(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_15'


class Mfm16(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_16'


class Mfm17(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_17'


class Mfm18(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_18'


class Mfm2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_2'


class Mfm24(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_24'


class Mfm25(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_25'


class Mfm26(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_26'


class Mfm27(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_27'


class Mfm28(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_28'


class Mfm29(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_29'


class Mfm3(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_3'


class Mfm30(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_30'


class Mfm31(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_31'


class Mfm32(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_32'


class Mfm33(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_33'


class Mfm34(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_34'


class Mfm35(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_35'


class Mfm36(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_36'


class Mfm37(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_37'


class Mfm38(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_38'


class Mfm39(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_39'


class Mfm4(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_4'


class Mfm40(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_40'


class Mfm41(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_41'


class Mfm42(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_42'


class Mfm43(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_43'


class Mfm44(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_44'


class Mfm45(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_45'


class Mfm46(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_46'


class Mfm47(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_47'


class Mfm48(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_48'


class Mfm49(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_49'


class Mfm5(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_5'


class Mfm50(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_50'


class Mfm51(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_51'


class Mfm52(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_52'


class Mfm53(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_53'


class Mfm54(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_54'


class Mfm55(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_55'


class Mfm56(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_56'


class Mfm57(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_57'


class Mfm58(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_58'


class Mfm59(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_59'


class Mfm6(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_6'


class Mfm60(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_60'


class Mfm61(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_61'


class Mfm62(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_62'


class Mfm63(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_63'


class Mfm64(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_64'


class Mfm65(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_65'


class Mfm66(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_66'


class Mfm67(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_67'


class Mfm68(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_68'


class Mfm69(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_69'


class Mfm7(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_7'


class Mfm70(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_70'


class Mfm71(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_71'


class Mfm72(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_72'


class Mfm73(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_73'


class Mfm74(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_74'


class Mfm75(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_75'


class Mfm76(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_76'


class Mfm77(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_77'


class Mfm78(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_78'


class Mfm79(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_79'


class Mfm8(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_8'


class Mfm80(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_80'


class Mfm81(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_81'


class Mfm82(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_82'


class Mfm83(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_83'


class Mfm9(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_active_power = models.FloatField(db_column='AVG_ACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_app_power = models.FloatField(db_column='AVG_APP_POWER', blank=True, null=True)  # Field name made lowercase.
    avg_current = models.FloatField(db_column='AVG_CURRENT', blank=True, null=True)  # Field name made lowercase.
    avg_pf = models.FloatField(db_column='AVG_PF', blank=True, null=True)  # Field name made lowercase.
    avg_reactive_power = models.FloatField(db_column='AVG_REACTIVE_POWER', blank=True, null=True)  # Field name made lowercase.
    b_current = models.FloatField(db_column='B_CURRENT', blank=True, null=True)  # Field name made lowercase.
    b_voltage = models.FloatField(db_column='B_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    br_voltage = models.FloatField(db_column='BR_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='FREQUENCY', blank=True, null=True)  # Field name made lowercase.
    r_current = models.FloatField(db_column='R_CURRENT', blank=True, null=True)  # Field name made lowercase.
    r_voltage = models.FloatField(db_column='R_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    ry_voltage = models.FloatField(db_column='RY_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    today_app_energy = models.FloatField(db_column='TODAY_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    tody_gen = models.FloatField(db_column='TODY_GEN', blank=True, null=True)  # Field name made lowercase.
    total_app_energy = models.FloatField(db_column='TOTAL_APP_ENERGY', blank=True, null=True)  # Field name made lowercase.
    total_gen = models.FloatField(db_column='TOTAL_GEN', blank=True, null=True)  # Field name made lowercase.
    y_current = models.FloatField(db_column='Y_CURRENT', blank=True, null=True)  # Field name made lowercase.
    y_voltage = models.FloatField(db_column='Y_VOLTAGE', blank=True, null=True)  # Field name made lowercase.
    yb_voltage = models.FloatField(db_column='YB_VOLTAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MFM_9'


class Sysmsgs(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventcol = models.CharField(db_column='EventCol', max_length=24, blank=True, null=True)  # Field name made lowercase.
    evnumcol = models.SmallIntegerField(db_column='EvNumCol', blank=True, null=True)  # Field name made lowercase.
    evdesccol = models.CharField(db_column='EvDescCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desccol = models.CharField(db_column='DescCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commcol = models.CharField(db_column='CommCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    durcol = models.IntegerField(db_column='DurCol', blank=True, null=True)  # Field name made lowercase.
    uniid = models.IntegerField(db_column='UniID', blank=True, null=True)  # Field name made lowercase.
    traid = models.IntegerField(db_column='TraID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SysMsgs'


class Wms2(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ambient_temp = models.FloatField(db_column='Ambient_temp', blank=True, null=True)  # Field name made lowercase.
    cumm_ghi = models.FloatField(db_column='Cumm_GHI', blank=True, null=True)  # Field name made lowercase.
    ghi = models.FloatField(db_column='GHI', blank=True, null=True)  # Field name made lowercase.
    module_temp = models.FloatField(db_column='Module_temp', blank=True, null=True)  # Field name made lowercase.
    peak_ambient_temp = models.FloatField(db_column='Peak_Ambient_temp', blank=True, null=True)  # Field name made lowercase.
    peak_module_temp = models.FloatField(db_column='Peak_Module_temp', blank=True, null=True)  # Field name made lowercase.
    wind_speed = models.FloatField(db_column='Wind_Speed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WMS_2'


class WmsMain1(models.Model):
    timecol = models.DateTimeField(db_column='TimeCol', blank=True, null=True)  # Field name made lowercase.
    mseccol = models.SmallIntegerField(db_column='MSecCol', blank=True, null=True)  # Field name made lowercase.
    localcol = models.DateTimeField(db_column='LocalCol', blank=True, null=True)  # Field name made lowercase.
    usercol = models.CharField(db_column='UserCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasoncol = models.CharField(db_column='ReasonCol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ghi = models.FloatField(db_column='GHI', blank=True, null=True)  # Field name made lowercase.
    cumm_ghi = models.FloatField(db_column='Cumm_GHI', blank=True, null=True)  # Field name made lowercase.
    wind_speed = models.FloatField(db_column='Wind_Speed', blank=True, null=True)  # Field name made lowercase.
    ambient_temp = models.FloatField(db_column='Ambient_temp', blank=True, null=True)  # Field name made lowercase.
    module_temp = models.FloatField(db_column='Module_temp', blank=True, null=True)  # Field name made lowercase.
    peak_ambient_temp = models.FloatField(db_column='Peak_Ambient_temp', blank=True, null=True)  # Field name made lowercase.
    peak_module_temp = models.FloatField(db_column='Peak_Module_temp', blank=True, null=True)  # Field name made lowercase.
    plant_pr = models.FloatField(db_column='Plant_PR', blank=True, null=True)  # Field name made lowercase.
    plant_cuf = models.FloatField(db_column='Plant_CUF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WMS_MAIN_1'
