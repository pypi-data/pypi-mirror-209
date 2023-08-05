"""
This module contains the abstract class for an SECC to retrieve data from the EVSE
(Electric Vehicle Supply Equipment).
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

from iso15118.shared.messages.datatypes import (
    DCEVSEChargeParameter,
    DCEVSEStatus,
    PVEAmount,
    PVEVEnergyRequest,
    PVEVMaxCurrent,
    PVEVMaxCurrentLimit,
    PVEVMaxVoltage,
    PVEVMaxVoltageLimit,
    PVEVSEMaxCurrentLimit,
    PVEVSEMaxPowerLimit,
    PVEVSEMaxVoltageLimit,
    PVEVSEPresentCurrent,
    PVEVSEPresentVoltage,
    PVEVTargetCurrent,
    PVEVTargetVoltage,
)
from iso15118.shared.messages.din_spec.datatypes import (
    SAScheduleTupleEntry as SAScheduleTupleEntryDINSPEC,
)
from iso15118.shared.messages.enums import (
    AuthorizationStatus,
    AuthorizationTokenType,
    ControlMode,
    CpState,
    EnergyTransferModeEnum,
    IsolationLevel,
    Protocol,
    ServiceV20,
    SessionStopAction,
)
from iso15118.shared.messages.iso15118_2.datatypes import (
    ACEVSEChargeParameter,
    ACEVSEStatus,
)
from iso15118.shared.messages.iso15118_2.datatypes import MeterInfo as MeterInfoV2
from iso15118.shared.messages.iso15118_2.datatypes import SAScheduleTuple
from iso15118.shared.messages.iso15118_20.ac import (
    ACChargeParameterDiscoveryResParams,
    BPTACChargeParameterDiscoveryResParams,
    BPTDynamicACChargeLoopResParams,
    BPTScheduledACChargeLoopResParams,
    DynamicACChargeLoopResParams,
    ScheduledACChargeLoopResParams,
)
from iso15118.shared.messages.iso15118_20.common_messages import (
    DynamicScheduleExchangeResParams,
    ProviderID,
    ScheduledScheduleExchangeResParams,
    ScheduleExchangeReq,
    SelectedEnergyService,
    ServiceList,
    ServiceParameterList,
)
from iso15118.shared.messages.iso15118_20.common_types import EVSEStatus, RationalNumber
from iso15118.shared.messages.iso15118_20.dc import (
    BPTDCChargeParameterDiscoveryResParams,
    BPTDynamicDCChargeLoopRes,
    BPTScheduledDCChargeLoopResParams,
    DCChargeParameterDiscoveryResParams,
    DynamicDCChargeLoopRes,
    ScheduledDCChargeLoopResParams,
)


@dataclass
class EVDataContext:
    dc_current: Optional[float] = None
    dc_voltage: Optional[float] = None
    ac_current: Optional[dict] = None  # {"l1": 10, "l2": 10, "l3": 10}
    ac_voltage: Optional[dict] = None  # {"l1": 230, "l2": 230, "l3": 230}
    soc: Optional[int] = None  # 0-100

    # from ISO 15118-20 AC
    departure_time: Optional[int] = None
    ev_target_energy_request: float = 0.0
    ev_max_energy_request: float = 0.0
    ev_min_energy_request: float = 0.0

    ev_max_charge_power: float = 0.0
    ev_max_charge_power_l2: Optional[float] = None
    ev_max_charge_power_l3: Optional[float] = None
    ev_min_charge_power: float = 0.0
    ev_min_charge_power_l2: Optional[float] = None
    ev_min_charge_power_l3: Optional[float] = None
    ev_present_active_power: float = 0.0
    ev_present_active_power_l2: Optional[float] = None
    ev_present_active_power_l3: Optional[float] = None
    ev_present_reactive_power: float = 0.0
    ev_present_reactive_power_l2: Optional[float] = None
    ev_present_reactive_power_l3: Optional[float] = None

    # BPT values
    ev_max_discharge_power: float = 0.0
    ev_max_discharge_power_l2: Optional[float] = None
    ev_max_discharge_power_l3: Optional[float] = None
    ev_min_discharge_power: float = 0.0
    ev_min_discharge_power_l2: Optional[float] = None
    ev_min_discharge_power_l3: Optional[float] = None
    ev_max_v2x_energy_request: Optional[float] = None
    ev_min_v2x_energy_request: Optional[float] = None

    def update(self, new: dict):
        self.__dict__.update(new)

    def as_dict(self):
        return self.__dict__


class ServiceStatus(str, Enum):
    READY = "ready"
    STARTING = "starting"
    STOPPING = "stopping"
    ERROR = "error"
    BUSY = "busy"


@dataclass
class EVChargeParamsLimits:
    ev_max_voltage: Optional[Union[PVEVMaxVoltageLimit, PVEVMaxVoltage]] = None
    ev_max_current: Optional[Union[PVEVMaxCurrentLimit, PVEVMaxCurrent]] = None
    e_amount: Optional[PVEAmount] = None
    ev_energy_request: Optional[PVEVEnergyRequest] = None


class EVSEControllerInterface(ABC):
    def __init__(self):
        self.ev_data_context = EVDataContext()
        self._selected_protocol = Optional[Protocol]

    def reset_ev_data_context(self):
        self.ev_data_context = EVDataContext()

    def get_ev_data_context(self) -> EVDataContext:
        return self.ev_data_context

    # ============================================================================
    # |             COMMON FUNCTIONS (FOR ALL ENERGY TRANSFER MODES)             |
    # ============================================================================

    @abstractmethod
    async def set_status(self, status: ServiceStatus) -> None:
        """
        Sets the new status for the EVSE Controller
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_id(self, protocol: Protocol) -> str:
        """
        Gets the ID of the EVSE (Electric Vehicle Supply Equipment), which is
        controlling the energy flow to the connector the EV is plugged into.

        Relevant for:
        - DIN SPEC 70121
        - ISO 15118-2
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_supported_energy_transfer_modes(
        self, protocol: Protocol
    ) -> List[EnergyTransferModeEnum]:
        """
        The available energy transfer modes, which depends on the socket the EV is
        connected to.

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_scheduled_se_params(
        self,
        selected_energy_service: SelectedEnergyService,
        schedule_exchange_req: ScheduleExchangeReq,
    ) -> Optional[ScheduledScheduleExchangeResParams]:
        """
        Gets the parameters for a ScheduleExchangeResponse, which correspond to the
        Scheduled control mode. If the parameters are not yet ready when requested,
        return None.

        Args:
            selected_energy_service: The energy services, which the EVCC selected.
                                     The selected parameter set, that is associated
                                     with that energy service, influences the
                                     parameters for the ScheduleExchangeRes
            schedule_exchange_req: The ScheduleExchangeReq, whose parameters influence
                                   the parameters for the ScheduleExchangeRes

        Returns:
            Parameters for the ScheduleExchangeRes in Scheduled control mode, if
            readily available. If you're still waiting for all parameters, return None.

        Relevant for:
        - ISO 15118-20
        """

    @abstractmethod
    async def get_dynamic_se_params(
        self,
        selected_energy_service: SelectedEnergyService,
        schedule_exchange_req: ScheduleExchangeReq,
    ) -> Optional[DynamicScheduleExchangeResParams]:
        """
        Gets the parameters for a ScheduleExchangeResponse, which correspond to the
        Dynamic control mode. If the parameters are not yet ready when requested,
        return None.

        Args:
            selected_energy_service: The energy services, which the EVCC selected.
                                     The selected parameter set, that is associated
                                     with that energy service, influences the
                                     parameters for the ScheduleExchangeRes
            schedule_exchange_req: The ScheduleExchangeReq, whose parameters influence
                                   the parameters for the ScheduleExchangeRes

        Returns:
            Parameters for the ScheduleExchangeRes in Dynamic control mode, if
            readily available. If you're still waiting for all parameters, return None.

        Relevant for:
        - ISO 15118-20
        """

    @abstractmethod
    async def get_energy_service_list(self) -> ServiceList:
        """
        The available energy transfer services

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    def is_eim_authorized(self) -> bool:
        """
        it returns true when an rfid authentication before plugging in.
        Relevant for:
        - ISO 15118-2
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def is_authorized(
        self,
        id_token: Optional[str] = None,
        id_token_type: Optional[AuthorizationTokenType] = None,
        certificate_chain: Optional[bytes] = None,
        hash_data: Optional[List[Dict[str, str]]] = None,
    ) -> AuthorizationStatus:
        """
        Provides the information on whether or not the user is authorized to charge at
        this EVSE. The auth token could be an RFID card, a whitelisted MAC address
        of the EV (Autocharge), a contract certificate (Plug & Charge), or a payment
        authorization via NFC or credit card.

        Relevant for:
        - DIN SPEC 70121
        - ISO 15118-2
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_sa_schedule_list(
        self,
        ev_charge_params_limits: EVChargeParamsLimits,
        max_schedule_entries: Optional[int],
        departure_time: int = 0,
    ) -> Optional[List[SAScheduleTuple]]:
        """
        Requests the charging schedule from a secondary actor (SA) like a
        charge point operator, if available. If no backend information is given
        regarding the restrictions imposed on an EV charging profile, then the
        charging schedule is solely influenced by the max rating of the charger
        and the ampacity of the charging cable.

        Args:
            ev_charge_params_limits: Lists the maximum limits of the EV: max_voltage,
                            max_current and e_amount(AC)/energy_requested(DC)
            max_schedule_entries: The maximum amount of schedule entries the EVCC
                                  can handle, or None if not provided
            departure_time: The departure time given in seconds from the time of
                            sending the ChargeParameterDiscoveryReq. If the
                            request doesn't provide a departure time, then this
                            implies the need to start charging immediately.

        Returns:
            A list of SAScheduleTupleEntry values to influence the EV's charging profile
            if the backend/charger can provide the information already, or None if
            the calculation is still ongoing.

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_sa_schedule_list_dinspec(
        self, max_schedule_entries: Optional[int], departure_time: int = 0
    ) -> Optional[List[SAScheduleTupleEntryDINSPEC]]:
        """
        Requests the charging schedule from a secondary actor (SA) like a
        charge point operator, if available. If no backend information is given
        regarding the restrictions imposed on an EV charging profile, then the
        charging schedule is solely influenced by the max rating of the charger
        and the ampacity of the charging cable.

        Args:
            max_schedule_entries: The maximum amount of schedule entries the EVCC
                                  can handle, or None if not provided
            departure_time: The departure time given in seconds from the time of
                            sending the ChargeParameterDiscoveryReq. If the
                            request doesn't provide a departure time, then this
                            implies the need to start charging immediately.

        Returns:
            A list of SAScheduleTupleEntry values to influence the EV's charging profile
            if the backend/charger can provide the information already, or None if
            the calculation is still ongoing.

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_meter_info_v2(self) -> MeterInfoV2:
        """
        Provides the MeterInfo from the EVSE's smart meter

        Returns:
            A MeterInfo instance, which contains the meter reading

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_meter_info_v20(self) -> MeterInfoV2:
        """
        Provides the MeterInfo from the EVSE's smart meter

        Returns:
            A MeterInfo instance, which contains the meter reading

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_supported_providers(self) -> Optional[List[ProviderID]]:
        """
        Provides a list of eMSPs (E-Mobility Service Providers) supported by the SECC.
        This allows EVCC to filter the list of contract certificates to be utilized
        during the authorization.

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def set_hlc_charging(self, is_ongoing: bool) -> None:
        """
        Notify that high level communication is ongoing or not.
        Args:
            is_ongoing (bool): whether hlc charging is ongoing or not.
        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_cp_state(self) -> CpState:
        """
        Returns current cp state

        Relevant for:
        - IEC 61851-1
        """
        raise NotImplementedError

    @abstractmethod
    async def service_renegotiation_supported(self) -> bool:
        """
        Whether or not service renegotiation is supported

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_service_parameter_list(
        self, service_id: int
    ) -> Optional[ServiceParameterList]:
        """
        Provides a list of parameters for a specific service ID for which the EVCC
        requests additional information.

        Args:
            service_id: The service ID, according to Table 204 (ISO 15118-20)

        Returns:
            A ServiceParameterList instance for the requested service ID, or None if
            that service is not supported.

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def stop_charger(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def is_contactor_opened(self) -> bool:
        """
        Sends a command to the SECC to get the contactor status is opened to terminate
        energy flow

        Relevant for:
        - all protocols
        """
        raise NotImplementedError

    @abstractmethod
    async def is_contactor_closed(self) -> bool:
        """
        Sends a command to the SECC to get the contactor status is closed

        Relevant for:
        - all protocols
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_status(self) -> Optional[EVSEStatus]:
        """
        Gets the status of the EVSE

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def set_present_protocol_state(self, state_name: str):
        """
        This method sets the present state of the charging protocol.

        Relevant for:
        - DIN SPEC 70121
        - ISO 15118-2
        """
        raise NotImplementedError

    def set_selected_protocol(self, protocol: Protocol) -> None:
        """Set the selected Protocol.

        Args:
            protocol: An EV communication protocol supported by Josev.
        """
        self._selected_protocol = protocol

    def get_selected_protocol(self) -> Protocol:
        """Get the selected Protocol."""
        return self._selected_protocol

    @abstractmethod
    async def send_charging_power_limits(
        self,
        protocol: Protocol,
        control_mode: ControlMode,
        selected_energy_service: ServiceV20,
    ) -> None:
        """
        This method shall merge the EV-EVSE charging power limits and send it

        Args:
            protocol: protocol selected (DIN, ISO 15118-2, ISO 15118-20_AC,..)
            control_mode: Control mode for this session - Scheduled/Dynamic
            selected_energy_service: Enum for this Service - AC/AC_BPT/DC/DC_BPT

        Returns: None

        """
        raise NotImplementedError

    # ============================================================================
    # |                          AC-SPECIFIC FUNCTIONS                           |
    # ============================================================================

    @abstractmethod
    async def get_ac_evse_status(self) -> ACEVSEStatus:
        """
        Gets the AC-specific EVSE status information

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_ac_charge_params_v2(self) -> ACEVSEChargeParameter:
        """
        Gets the AC-specific EVSE charge parameter (for ChargeParameterDiscoveryRes)

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_ac_charge_params_v20(
        self, selected_service: ServiceV20
    ) -> Union[
        ACChargeParameterDiscoveryResParams, BPTACChargeParameterDiscoveryResParams
    ]:
        """
        Gets the charge parameters needed for a ChargeParameterDiscoveryRes for
        AC/AC_BPT charging.

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_ac_charge_loop_params_v20(
        self, control_mode: ControlMode, selected_service: ServiceV20
    ) -> Union[
        ScheduledACChargeLoopResParams,
        BPTScheduledACChargeLoopResParams,
        DynamicACChargeLoopResParams,
        BPTDynamicACChargeLoopResParams,
    ]:
        """
        Gets the parameters for the ACChargeLoopRes for the currently set control mode
         and service.
        Args:
            control_mode: Control mode for this session - Scheduled/Dynamic
            selected_service: Enum for this Service - AC/AC_BPT
        Returns:
            ChargeLoop params depending on the selected mode. Return object could be
            one of the following types:
            [
                ScheduledACChargeLoopResParams,
                BPTScheduledACChargeLoopResParams,
                DynamicACChargeLoopResParams,
                BPTDynamicACChargeLoopResParams,
            ]
        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    # ============================================================================
    # |                          DC-SPECIFIC FUNCTIONS                           |
    # ============================================================================

    @abstractmethod
    async def get_dc_evse_status(self) -> DCEVSEStatus:
        """
        Gets the DC-specific EVSE status information

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_dc_evse_charge_parameter(self) -> DCEVSEChargeParameter:
        """
        Gets the DC-specific EVSE charge parameter (for ChargeParameterDiscoveryRes)

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_present_voltage(
        self, protocol: Protocol
    ) -> Union[PVEVSEPresentVoltage, RationalNumber]:
        """
        Gets the presently available voltage at the EVSE

        Relevant for:
        - ISO 15118-2
        - ISO 15118-20
        - DINSPEC
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_present_current(
        self, protocol: Protocol
    ) -> Union[PVEVSEPresentCurrent, RationalNumber]:
        """
        Gets the presently available voltage at the EVSE

        Relevant for:
        - ISO 15118-2
        - ISO 15118-20
        - DINSPEC
        """
        raise NotImplementedError

    @abstractmethod
    async def set_precharge(
        self, voltage: PVEVTargetVoltage, current: PVEVTargetCurrent
    ):
        """
        Sets the precharge information coming from the EV.
        The charger must adapt it's output voltage to the requested voltage from the EV.
        The current may not exceed 2A (according 61851-23)

        Relevant for:
        - DIN SPEC 70121
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def start_cable_check(self):
        """
        This method is called at the beginning of the state CableCheck.
        It requests the charger to perform a CableCheck

        Relevant for:
        - DIN SPEC 70121
        - ISO 15118-2
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_cable_check_status(self) -> Union[IsolationLevel, None]:
        """
        This method is called at the beginning of the state CableCheck.
        Gets's the status of a previously started CableCheck

        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def send_charging_command(
        self, voltage: PVEVTargetVoltage, current: PVEVTargetCurrent
    ):
        """
        This method is called in the state CurrentDemand. The values target current
        and target voltage from the EV are passed.
        These information must be provided for the charger's power electronics.

        Relevant for:
        - DIN SPEC 70121
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def is_evse_current_limit_achieved(self) -> bool:
        """
        Returns true if the current limit of the charger has achieved

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def is_evse_voltage_limit_achieved(self) -> bool:
        """
        Returns true if the current limit of the charger has achieved

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def is_evse_power_limit_achieved(self) -> bool:
        """
        Returns true if the current limit of the charger has achieved

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_max_voltage_limit(self) -> PVEVSEMaxVoltageLimit:
        """
        Gets the max voltage that can be provided by the charger

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_max_current_limit(self) -> PVEVSEMaxCurrentLimit:
        """
        Gets the max current that can be provided by the charger

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_dc_charge_params_v20(
        self, selected_service: ServiceV20
    ) -> Union[
        DCChargeParameterDiscoveryResParams, BPTDCChargeParameterDiscoveryResParams
    ]:
        """
        Gets the charge parameters needed for a ChargeParameterDiscoveryRes for
        DC charging.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_evse_max_power_limit(self) -> PVEVSEMaxPowerLimit:
        """
        Gets the max power that can be provided by the charger

        Relevant for:
        - ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def get_dc_charge_loop_params_v20(
        self, control_mode: ControlMode, selected_service: ServiceV20
    ) -> Union[
        ScheduledDCChargeLoopResParams,
        BPTScheduledDCChargeLoopResParams,
        DynamicDCChargeLoopRes,
        BPTDynamicDCChargeLoopRes,
    ]:
        """
        Gets the parameters for the DCChargeLoopRes for the currently set control mode
         and service.
        Args:
            control_mode: Control mode for this session - Scheduled/Dynamic
            selected_service: Enum for this Service - DC/DC_BPT
        Returns:
            ChargeLoop params depending on the selected mode. Return object could be
            one of the following types:
            [
                ScheduledDCChargeLoopResParams,
                BPTScheduledDCChargeLoopResParams,
                DynamicDCChargeLoopRes,
                BPTDynamicDCChargeLoopRes,
            ]
        Relevant for:
        - ISO 15118-20
        """
        raise NotImplementedError

    @abstractmethod
    async def get_15118_ev_certificate(
        self, base64_encoded_cert_installation_req: str, namespace: str
    ) -> str:
        """
        Used to fetch base64 encoded CertificateInstallationRes from CPO backend.
        Args:
         base64_encoded_cert_installation_req : This is the CertificateInstallationReq
         from the EV in base64 encoded form.
         namespace: This would be the namespace to be passed to the backend and depends
          on the protocol.
         15118-2:  "urn:iso:15118:2:2013:MsgDef"
         15118-20: "urn:iso:std:iso:15118:-20:CommonMessages"
        Returns:
         CertificateInstallationRes EXI stream in base64 encoded form.

        Relevant for:
        - ISO 15118-20 and ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    async def update_data_link(self, action: SessionStopAction) -> None:
        """
        Called when EV requires termination or pausing of the charging session.
        Args:
            action : SessionStopAction
        Relevant for:
        - ISO 15118-20 and ISO 15118-2
        """
        raise NotImplementedError

    @abstractmethod
    def ready_to_charge(self) -> bool:
        """
        Used by Authorization state to indicate if we are
        ready to start charging.
        """
        raise NotImplementedError
